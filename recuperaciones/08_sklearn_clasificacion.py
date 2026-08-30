"""Demo de scikit-learn: pipeline y matriz de confusión."""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

x = np.array(
    [
        [0.8, 1.0], [1.0, 1.1], [1.2, 0.9], [1.4, 1.3],
        [2.7, 2.8], [3.0, 2.6], [3.2, 3.1], [2.8, 3.3],
    ]
)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

modelo = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
modelo.fit(x, y)
prediccion = modelo.predict(x)

print("predicciones:", prediccion)
print("matriz de confusión:\n", confusion_matrix(y, prediccion))
print("caso nuevo [2.0, 2.0]:", modelo.predict([[2.0, 2.0]])[0])
