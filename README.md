Smart House Price Predictor

A machine learning web application that predicts house prices based on user inputs such as area size, number of bedrooms, and number of bathrooms. The system provides instant predictions through a simple web interface.

Project Overview

This application allows users to enter property details and predicts house prices using a trained machine learning model. It follows a machine learning workflow that includes:

- Data preprocessing and feature engineering
- Model training using regression algorithms
- Model evaluation and model persistence
- Flask integration
- Frontend integration for real-time predictions

Features

- House Price Prediction: Predicts house prices using a trained regression model.
- Simple Web Interface: Allows users to enter property details and get a prediction.
- Instant Predictions: Returns the predicted house price after submitting the input.
- Clean Project Structure: Separates the data, model, frontend, and backend files.
- Flask Integration: Uses Flask to connect the machine learning model with the web application.

Dataset Information

The housing dataset is used to train the regression model.

Features:

- Area size (sq ft)
- Number of bedrooms
- Number of bathrooms

Target:

- House price

Project Structure

Smart-House-Price-Predictor/
│
├── data/
│   └── house_data.csv
│
├── model/
│   └── train_model.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── assets/
│   └── homepage.png
│
├── house_price_model.pkl
├── scaler.pkl
├── app.py
├── requirements.txt
└── README.md

Installation and Running Guide

Clone the repository and move into the project directory:

cd Smart-House-Price-Predictor

Install the required dependencies:

pip install -r requirements.txt

Train the machine learning model:

python model/train_model.py

Run the Flask application:

python app.py

Then open the local address provided by Flask in your browser.

Requirements

The project uses the following Python libraries:

Flask
pandas
scikit-learn
numpy
joblib

The exact versions should be specified in "requirements.txt" based on the environment used to develop and test the project.
