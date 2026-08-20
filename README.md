# Student Marks Predictor

A simple machine learning web application that predicts a student's expected score based on the number of hours studied.

## Features

- User-friendly web interface
- Study-hour input
- Score prediction using Linear Regression
- Flask-based web application
- CSV-based training dataset
- Basic HTML and CSS frontend

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- HTML
- CSS

## How It Works

The application uses a Linear Regression model trained on a dataset containing study hours and corresponding scores.

The workflow is:

User enters study hours
→ Flask receives the input
→ Linear Regression model predicts the score
→ Predicted score is displayed on the webpage

## Project Structure

```text
student-marks-predictor/
├── app.py
├── model.py
├── student_scores.csv
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css