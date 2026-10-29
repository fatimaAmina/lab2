import numpy as np
from sklearn.linear_model import LinearRegression
hours = np.array[1, 2, 3, 4, 5].reshape(-1, 1)
scores = np.array([50, 60, 68, 80, 87])
model = LinearRegression()
model.fit(hours,scores)
a1 = model.intercept_
a2 = model.coef_[0]
print(f"score = {a1:.1f}+{a2:.1f}*hours")
new_hours = np.array([3.5,6]).reshape(-1,1)
predictons = model.predict(new_hours)
print(f"3.5 hours:{predictons[0]:.1f}")
print(f"6 hours:{predictons[1]:.1f}")