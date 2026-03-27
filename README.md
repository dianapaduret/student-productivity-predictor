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

##  Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

##  Project Structure
student-productivity-predictor/
 - backend: main.py # FastAPI backend (prediction API)
 - frontend: app.py # Streamlit user interface
 - model: productivity_model.pkl # trained ML model
 - data: student_productivity.csv # dataset
 - notebooks: eda.ipynb # data exploration; model_day2.ipynb # model training
 - requirements.txt # dependencies
 - README.md # project documentation
 - .gitignore # ignored files
