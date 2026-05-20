import joblib
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from preprocess import load_and_preprocess

X_train, X_test, y_train, y_test, feature_names = load_and_preprocess("data/raw/transactions.csv")

model = joblib.load("models/xgboost_fraud_model.pkl")

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))