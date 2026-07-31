# AdaBoost is a boosting algorithm that combines multiple weak learners to create a strong
# classifier by focusing more on previously misclassified samples.

# Import libraries
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Base learner (Decision Stump)
base_model = DecisionTreeClassifier(
    max_depth=1, # Depth means how many levels the tree can have ,normally this seems weak exactly AdaBoost wants weak models.
    random_state=42
)

# Create AdaBoost model
model = AdaBoostClassifier(
    estimator=base_model,
    n_estimators=50, # train 50 weak learners
    learning_rate=1.0,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))