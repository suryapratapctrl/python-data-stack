import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

df["species"].unique()

df.isnull().sum()

# we need only two so we are removing one which setosa


df=df[df["species"] != "setosa"]

df["species"] = df["species"].map({"versicolor": 0, "virginica": 1})

## split dataset into independent and dependent features
X = df.iloc[:, :-1]
y = df.iloc[:, -1]


#
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()


from sklearn.model_selection import GridSearchCV

parameter = {
    "penalty": ["l1", "l2"],
    "C": [
        1,
        2,
        3,
        4,
        5,
        6,
        10,
        20,
        30,
        40,
        50,
    ],
    "max_iter": [100, 200, 300],
}

classifier_regressor = GridSearchCV(classifier, param_grid=parameter, scoring="accuracy", cv=5)

classifier_regressor.fit(X_train, y_train)

print(classifier_regressor.best_params_)
print(classifier_regressor.best_score_)



#prediction
y_pred=classifier_regressor.predict(X_test)


#accracy score
from sklearn.metrics import accuracy_score,classification_report
score=accuracy_score(y_pred,y_test)
print(score)

print(classification_report(y_pred,y_test))


# eda -> it is the process of understanding your data before training a machine learning model.
sns.pairplot(df,hue='species')
plt.show()

# ruff: noqa: E402
