"""Demo de scikit-learn: regresión con conjunto de prueba."""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

generador = np.random.default_rng(7)
x = np.linspace(0, 10, 40).reshape(-1, 1)
y = 2.5 * x[:, 0] + 1.2 + generador.normal(0, 0.8, size=len(x))

x_entreno, x_prueba, y_entreno, y_prueba = train_test_split(
    x, y, test_size=0.25, random_state=7
)
modelo = LinearRegression().fit(x_entreno, y_entreno)
prediccion = modelo.predict(x_prueba)

print("coeficiente:", modelo.coef_[0])
print("intercepto:", modelo.intercept_)
print("error absoluto medio:", mean_absolute_error(y_prueba, prediccion))
