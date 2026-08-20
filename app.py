from flask import Flask, render_template, request
from model import predict_score

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        prediction = predict_score(hours)

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)