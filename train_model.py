# Smart House Price Predictor
# خطوة تدريب نموذج التنبؤ بأسعار المنازل باستخدام الـ Linear Regression

import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# 1. تجهيز بيانات التدريب (المساحة، عدد الغرف) والأسعار
X = np.array([[1200, 2], [1500, 3], [2000, 4], [800, 1], [2500, 4], [1800, 3]])
y = np.array([150000, 200000, 300000, 90000, 400000, 250000])

# 2. إنشاء نموذج الانحدار الخطي وتدريبه
model = LinearRegression()
model.fit(X, y)
print("تم تدريب الموديل بنجاح!")

# 3. حفظ الموديل لاستخدامه في تطبيق الويب
joblib.dump(model, 'house_price_model.pkl')
print("تم حفظ الموديل في ملف house_price_model.pkl")
