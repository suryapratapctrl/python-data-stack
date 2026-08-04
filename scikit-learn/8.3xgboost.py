# XGBoost is an optimized implementation of Gradient Boosting that includes regularization,
# efficient tree construction, and parallel processing to improve accuracy and speed

# XGBoost is better version of Gradient Boosting that adds regularization, efficient tree construction, parallel 
# split finding, automatic handling of missing values, making it faster, more accurate & less prone to overfitting

# Import libraries
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# Load dataset
data = load_wine()

# Features and target
X = data.data
y = data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create XGBoost model
model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
    eval_metric="mlogloss"
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Model accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Detailed performance report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# eval_metric is a parameter in XGBoost that specifies the evaluation metric 
# used to measure the model's performance during training

#  Different tasks require different metrics, such as logloss for binary 
# classification, mlogloss for multi-class classification and rmse for regression
