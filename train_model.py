import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

# Example training data (marks in 6 subjects + attendance)
X = np.array([
    [80, 75, 70, 85, 90, 78, 95],
    [30, 25, 28, 35, 40, 32, 60],
    [60, 55, 58, 65, 62, 59, 80],
    [90, 92, 88, 95, 96, 91, 98],
    [45, 50, 42, 48, 46, 44, 70],
    [70, 65, 68, 72, 74, 69, 85]
])

# Labels: 1 = Pass, 0 = Fail
y = [1, 0, 1, 1, 0, 1]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("✅ model.pkl has been created successfully")
