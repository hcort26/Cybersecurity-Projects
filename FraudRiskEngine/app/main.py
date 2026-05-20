from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import glob

app = FastAPI()

model = joblib.load("models/xgboost_fraud_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

DATA_FOLDER = "data/raw"
SCORED_FOLDER = "data/scored"

os.makedirs(SCORED_FOLDER, exist_ok=True)


class Transaction(BaseModel):
    account_id: str
    timestamp: str
    amount: float
    location: str
    device_type: str
    transaction_velocity: int
    is_foreign_transaction: int
    location_change_since_last_tx: int
    new_device_used: int
    failed_login_attempts: int
    merchant_risk_score: float
    account_age_days: int
    amount_vs_avg: float
    time_of_day: int


def preprocess_for_model(df: pd.DataFrame) -> pd.DataFrame:
    df = pd.get_dummies(df, drop_first=True)

    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]
    return df


@app.get("/")
def home():
    return {"message": "Fraud Risk Engine API is running"}


@app.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.model_dump()])
    data = preprocess_for_model(data)

    risk_score = float(model.predict_proba(data)[0][1])

    return {
        "fraud_risk_score": risk_score,
        "flagged": risk_score >= 0.7
    }


@app.get("/score-account/{account_id}")
def score_account(account_id: str):
    file_path = os.path.join(DATA_FOLDER, f"{account_id}_transactions.csv")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Account file not found: {file_path}")

    df = pd.read_csv(file_path)
    original_df = df.copy()

    X = df.drop(columns=["fraud"], errors="ignore")
    X = preprocess_for_model(X)

    fraud_scores = model.predict_proba(X)[:, 1]
    flagged = fraud_scores >= 0.7

    original_df["fraud_risk_score"] = fraud_scores
    original_df["flagged"] = flagged

    output_path = os.path.join(SCORED_FOLDER, f"{account_id}_scored.csv")
    original_df.to_csv(output_path, index=False)

    flagged_rows = original_df[original_df["flagged"] == True]

    return {
        "account_id": account_id,
        "total_transactions": int(len(original_df)),
        "flagged_transactions": int(flagged.sum()),
        "average_fraud_risk_score": round(float(original_df["fraud_risk_score"].mean()), 4),
        "scored_file": output_path,
        "top_flagged_transactions": flagged_rows.sort_values(
            "fraud_risk_score", ascending=False
        ).head(5).to_dict(orient="records")
    }


@app.get("/score-all-accounts")
def score_all_accounts():
    account_files = glob.glob(os.path.join(DATA_FOLDER, "acct_*_transactions.csv"))

    if not account_files:
        raise HTTPException(status_code=404, detail="No account transaction files found.")

    summary = []

    for file_path in sorted(account_files):
        df = pd.read_csv(file_path)
        original_df = df.copy()

        X = df.drop(columns=["fraud"], errors="ignore")
        X = preprocess_for_model(X)

        fraud_scores = model.predict_proba(X)[:, 1]
        flagged = fraud_scores >= 0.7

        original_df["fraud_risk_score"] = fraud_scores
        original_df["flagged"] = flagged

        account_id = original_df["account_id"].iloc[0]
        output_path = os.path.join(SCORED_FOLDER, f"{account_id}_scored.csv")
        original_df.to_csv(output_path, index=False)

        summary.append({
            "account_id": account_id,
            "total_transactions": int(len(original_df)),
            "flagged_transactions": int(flagged.sum()),
            "average_fraud_risk_score": round(float(original_df["fraud_risk_score"].mean()), 4),
            "scored_file": output_path
        })

    return {
        "accounts_scored": len(summary),
        "results": summary
    }