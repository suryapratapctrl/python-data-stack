# Decision Tree using Post-Pruning ->in post pruning first we build tree then remove unnecessary branches
# Iris dataset is used because it is small and easy to understand.
# Pruning reduces overfitting by removing unnecessary branches.


import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)


from sklearn.tree import DecisionTreeClassifier

# postprunning
treemodel = DecisionTreeClassifier(
    random_state=42, max_depth=2
)  #  random_state is a seed value that controls randomness in machine learning algorithms

treemodel.fit(X_train, y_train)

from sklearn import tree

plt.figure(figsize=(8, 5))
tree.plot_tree(treemodel, filled=True)

plt.show()


# prediction
y_pred = treemodel.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report

score = accuracy_score(y_pred, y_test)
print(score)


print(classification_report(y_pred, y_test))


# ruff: noqa: E402


# -------------------- Notes --------------------

# Why do we need pruning?
# Sometimes a Decision Tree keeps growing until it classifies
# almost every training example perfectly.
# This causes overfitting, where the model performs well on
# training data but poorly on new unseen data.

# What is Post-Pruning?
# Post-Pruning first builds the complete Decision Tree and then
# removes unnecessary branches to reduce overfitting.

# What is ccp_alpha?
# ccp_alpha stands for Cost Complexity Pruning Alpha.
# It controls how much pruning is applied to the Decision Tree.

# ccp_alpha = 0
# -> No pruning (Full Decision Tree)

# Small ccp_alpha
# -> Removes only a few unnecessary branches.

# Large ccp_alpha
# -> Removes more branches, making the tree simpler.
# -> If too large, it may cause underfitting.

# cost_complexity_pruning_path() automatically calculates
# all possible ccp_alpha values for the Decision Tree.

# Example:
# ccp_alphas = [0.0, 0.002, 0.005, 0.01, 0.03]

# We do not know which ccp_alpha gives the best result.
# Therefore, we train one Decision Tree for every ccp_alpha,
# calculate its accuracy, and choose the model with the
# highest test accuracy.

# Workflow:
# 1. Build the complete Decision Tree.
# 2. Get all possible ccp_alpha values.
# 3. Train one tree for each ccp_alpha.
# 4. Compare their accuracies.
# 5. Select the tree with the highest accuracy

