#  Student Productivity Predictor

An end-to-end machine learning application that predicts a student's productivity score based on daily habits such as sleep, phone usage, and study time.

---

##  Project Overview

This project uses a regression model trained on student behavioral data to estimate productivity levels.

The system includes:
-  Data analysis and model training (Jupyter Notebook)
-  Backend API built with FastAPI
-  Interactive frontend built with Streamlit

---

##  Features

- Predict productivity score in real-time
- Interactive sliders for user input
- Clear feedback: Low / Medium / High productivity
- Full ML pipeline from data to deployment

---

## Model

- Algorithm: Linear Regression
- Features:
  - Sleep hours
  - Phone usage hours
  - Study hours per day
- Target: Productivity score

---


##  Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

## Project Structure

```text
student-productivity-predictor/
│
├── backend/
│ └── main.py # FastAPI backend
│
├── frontend/
│ └── app.py # Streamlit UI
│
├── model/
│ └── productivity_model.pkl
│
├── data/
│ ├── student_productivity.csv
│ └── project_cleaned_day1.csv
│
├── notebooks/
│ ├── eda.ipynb
│ └── model_day2.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
