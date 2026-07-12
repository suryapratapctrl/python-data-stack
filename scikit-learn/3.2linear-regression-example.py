import pandas as pd
from sklearn.datasets import load_diabetes
import numpy as np




# Load the dataset
df=load_diabetes()

# Convert to DataFrame
dataset= pd.DataFrame(df.data, columns=df.feature_names)
print(dataset)
print(dataset.head())

#indenpendent features and dependent features
X=dataset
y=df.target

# train test split

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

# standardizing the dataset
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

# Learn scaling parameters from training data  .fit_transform() (learn + apply)

X_train=scaler.fit_transform(X_train)

#  X_test = scaler.fit_transform(X_test)   ❌ Wrong because data leakage

# Apply the same parameters to test data  . transform() (apply only)

X_test=scaler.transform(X_test)


# importing linear regression

from sklearn.linear_model import LinearRegression



# cross validation
from sklearn.model_selection import cross_val_score

regression=LinearRegression()
regression.fit(X_train,y_train)

mse=cross_val_score(regression,X_train,y_train,scoring='neg_mean_squared_error',cv=5)
print(mse)

print(np.mean(mse))


# make the prediction

reg_pred=regression.predict(X_test)


from sklearn.metrics import r2_score

score=r2_score(y_test, reg_pred)
print(score)


# ruff: noqa: E402

