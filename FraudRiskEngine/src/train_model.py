import os
import joblib
from xgboost import XGBClassifier
from src.preprocess import load_and_preprocess

DATA_PATH = "data/raw/all_accounts.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "xgboost_fraud_model.pkl")
FEATURES_PATH = os.path.join(MODEL_DIR, "feature_names.pkl")

def main():
    print("Loading and preprocessing data...")
    X_train, X_test, y_train, y_test, feature_names = load_and_preprocess(DATA_PATH)

    print("Creating models directory if it does not exist...")
    os.makedirs(MODEL_DIR, exist_ok=True)

    print("Training XGBoost model...")
    model = XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=42
    )

    model.fit(X_train, y_train)

    print(f"Saving model to {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)

    print(f"Saving feature names to {FEATURES_PATH}")
    joblib.dump(feature_names, FEATURES_PATH)

    print("Done.")
    print("Saved files:")
    print(MODEL_PATH)
    print(FEATURES_PATH)

if __name__ == "__main__":
    main()