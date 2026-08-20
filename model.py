import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model():
    data = pd.read_csv("student_scores.csv")

    X = data[["Hours"]]
    y = data["Scores"]

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict_score(hours):
    model = train_model()
    prediction = model.predict([[hours]])

    return round(float(prediction[0]), 2)