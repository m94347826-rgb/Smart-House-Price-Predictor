from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model using the exact filename on GitHub
model = joblib.load('house_price_model (7).pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get sqft and bedrooms matching our model features
        sqft = float(request.form['sqft'])
        bedrooms = int(request.form['bedrooms'])
        
        # Prepare features for prediction
        features = np.array([[sqft, bedrooms]])
        prediction = model.predict(features)
        output = round(prediction[0], 2)
        
        return render_template('index.html', prediction_text=f'Estimated House Price: ${output:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error in input values: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
