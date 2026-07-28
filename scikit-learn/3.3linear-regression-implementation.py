import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# load dataset
data = pd.read_csv("Students Performance Dataset.csv")


# input and output
X = data[
    ["Study_Hours_per_Week"]
]  # X -> Input features (always 2D DataFrame, even with one column)
y = data["Final_Score"]  # y -> Target/output (1D Series)

# train model
model = LinearRegression()
model.fit(X, y)
predicted_score = model.predict(X)

# valid regression metrics
mse = mean_squared_error(y, predicted_score)
mae = mean_absolute_error(y, predicted_score)
rmse = np.sqrt(mse)
r2 = r2_score(y, predicted_score)

# show results
print("mean absolute error (MAE): ", round(mae, 3))
print("mean square error (MSE): ", round(mse, 3))
print("Root mean square error (RMSE): ", round(rmse, 2))
print("R^2 score (model accuracy): ", round(r2, 3))  # closer to 1 = better

# histogram
plt.figure(figsize=(10, 6))
plt.hist(data["Final_Score"], bins=30, color="skyblue", edgecolor="black")
plt.title("Distribution of final exam score")
plt.xlabel("final exam score")
plt.ylabel("number of students")
plt.grid(True)
plt.show()

# scatter + regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color="blue", label="Actual Scores")
plt.plot(X, predicted_score, color="red", label="Predicted Scores (Regression Line)")
plt.title("Model Prediction VS Actual Score")
plt.xlabel("Study Hours per Week")
plt.ylabel("Final Score")
plt.legend()
plt.grid(True)
plt.show()


new_hours = 9  # Example: Predicting for  study hours per week
predicted_final_score = model.predict([[new_hours]])
print(
    f"Predicted final score for {new_hours} hours per week: {predicted_final_score} score"
)
