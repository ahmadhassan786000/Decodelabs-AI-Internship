from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_and_split_data(test_size=0.2, random_state=42):
    data_path = Path(__file__).resolve().parents[1] / "data" / "iris.csv"
    df = pd.read_csv(data_path)

    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        shuffle=True,
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test
