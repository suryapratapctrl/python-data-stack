# Decision Tree using Pre-Pruning
#large dataset

from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

treemodel= DecisionTreeClassifier(random_state=42)

parameters = {
    'criterion': ['gini', 'entropy','log_loss'],
    'max_depth': [2,3,4,5,None],
    'min_samples_split': [2,5,10],
    'min_samples_leaf': [1,2,4],
    'max_features':['auto','sqrt','log2'],
    'splitter':['best','random']
}

grid = GridSearchCV(
    treemodel,
    param_grid=parameters,
    scoring='accuracy',
    cv=5
)

grid.fit(X_train, y_train)

print("Best Parameters")
print(grid.best_params_)

print("Best Accuracy")
print(grid.best_score_)


y_pred = grid.predict(X_test)


from sklearn.metrics import accuracy_score, classification_report

print("Accuracy")
print(accuracy_score( y_pred,y_test))

print(classification_report(y_test, y_pred))


import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10,7))

plot_tree(
    grid.best_estimator_,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.show()


# ruff: noqa: E402

# Gini Index: Measures the impurity of a node in a Decision Tree.
# A lower Gini value indicates a better and purer split.

# Entropy: Measures the uncertainty or randomness of a node in a Decision Tree.
# A lower Entropy value indicates a better and purer split.

