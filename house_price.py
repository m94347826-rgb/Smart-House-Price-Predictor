import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

X = np.array([[1200, 2], [1500, 3], [2000, 4], [800, 1], [2500, 4], [1800, 3]])
y = np.array([150000, 200000, 300000, 90000, 400000, 250000])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'house_price_model.pkl')

