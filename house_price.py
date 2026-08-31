# ==========================================
# مشروع تنبؤ أسعار المنازل (Smart House Price Predictor)
# ملف تدريب وبناء النموذج الرياضي
# ==========================================

import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

print("جاري تحميل وإعداد بيانات التدريب للمنازل...")
# بيانات المساحة وعدد الغرف
X = np.array([[1200, 2], [1500, 3], [2000, 4], [800, 1], [2500, 4], [1800, 3]])
# أسعار المنازل المقابلة
y = np.array([150000, 200000, 300000, 90000, 400000, 250000])

print("بناء وتدريب نموذج الانحدار الخطي (Linear Regression)...")
model = LinearRegression()
model.fit(X, y)

print("تدريب النموذج تم بنجاح، جاري حفظه...")
# حفظ الموديل النهائي في ملف pkl للاستخدام في تطبيق الويب
joblib.dump(model, 'house_price_model.pkl')
print("تم حفظ النموذج بنجاح في ملف house_price_model.pkl!")
