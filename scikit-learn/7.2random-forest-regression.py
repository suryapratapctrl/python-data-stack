import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("Students Performance Dataset.csv")

# Input features and target
X = data[[
    "Study_Hours_per_Week",
    "Attendance (%)",
    "Midterm_Score",
    "Assignments_Avg",
    "Quizzes_Avg",
    "Participation_Score",
    "Projects_Score",
    "Sleep_Hours_per_Night"
]]
y = data["Final_Score"]

#print(data.isnull().sum())

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print("R² Score:", round(r2_score(y_test, predictions), 2))
print("Mean Squared Error:", round(mean_squared_error(y_test, predictions), 2))
print(X.corrwith(y)) # this check the correlation between each input feature and the target variable
# The model gives a low R² score because the selected features have
# very weak correlation with the target (Final_Score), making accurate
# prediction difficult.

