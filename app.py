from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['area']),
            int(request.form['bedrooms']),
            int(request.form['bathrooms'])
        ]
        final_features = [np.array(features)]
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'السعر المتوقع للمنزل هو: ${output:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'حدث خطأ في المدخلات: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
