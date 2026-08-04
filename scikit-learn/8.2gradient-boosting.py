# it is also an ensemble learning algorithm that builds a strong predictive model by training weak learners sequentially
# each new model is trained to minimize the errors (residuals) made by the previous models using gradient descent optimization

from sklearn.datasets import load_wine
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Load dataset
data=load_wine()

X=data.data   # contains all the feature columns (X)    this is a preloaded dataset thats why do not need write 
y=data.target # contains the target column (y)          features explicitly cuz they are already seperated

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Gradient Boosting Model
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Report
print(classification_report(y_test, y_pred))

