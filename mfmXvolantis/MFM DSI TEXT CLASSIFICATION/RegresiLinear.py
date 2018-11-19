import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[3],[4],[6],[7],[8],[9]])
t = np.array([1,3,4,6,8,8])

regr = LinearRegression()
regr.fit(X,t)

# Nilai Koefisien
print ("Parameter bias  wo : %s" %regr.intercept_)
print ("Parameter bobot w  : %s" %regr.coef_)

# Prediksi Nilai Baru
print ("Prediksi nilai x = 5 : %s" %regr.predict(5))
