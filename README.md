# Smart House Price Predictor 🏠

A complete machine learning web application that predicts house prices based on user inputs such as area size, number of bedrooms, and bathrooms. The system provides instant predictions through an intuitive web interface.

## Project Overview

This application allows users to enter property details and predicts house prices using a trained machine learning model.
It follows a complete machine learning lifecycle:
- Data preprocessing and feature engineering
- Model training using regression algorithms
- Model evaluation and persistence
- Deployment using Flask
- Professional frontend integration for real-time predictions

## Features

- **Predicts House Prices via Machine Learning:** Predicts house prices using a trained regression model.
- **Simple, Fast, and Interactive Web Interface:** Responsive design for entering property details.
- **Instant Price Predictions:** Users receive expected house prices immediately upon form submission.
- **Clean Project Structure:** Well-organized directories for data, models, frontend templates, and backend logic.
- **Built with Flask Integration:** The backend is built using the Flask web framework.
- **Cloud Deployment Ready:** Easily deployable on standard cloud computing platforms.

## Dataset Information

The housing dataset used to train the regression model.

**Features:**
- Area size (sq ft)
- Number of bedrooms
- Number of bathrooms

**Target House Price:**
The model predicts house prices based on these characteristics.

## Project Structure

```text
house-price-prediction-web-app/
├── data/
│   └── house_data.csv
├── model/
│   └── train_model.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── assets/
│   └── homepage.png
├── house_price_model.pkl
├── scaler.pkl
├── app.py
├── requirements.txt
└── README.md
```
git clone https://github.com/m943/Smart-House-Price-Predictor.git
cd Smart-House-Price-Predictor

pip install -r requirements.txt
python model/train_model.py
model/house_price_model.pkl
python app.py
Flask==2.3.5
pandas==2.1.1
scikit-learn==1.3.2
numpy==1.26.5
joblib==1.3.2
```
