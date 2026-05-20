import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess(filepath):
    df = pd.read_csv(filepath)

    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, X.columns.tolist()