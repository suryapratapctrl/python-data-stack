# feature scaling -> is the process of bringing numerical features to a similar scale so that machine learning algorithms perform better
# 1. Standardization (StandardScaler) -> it is good for algorithms like Logistic Regression, SVM, KNN, PCA, and Neural Networks
# 2. Normalization (MinMaxScaler) -> it is good when you want all values in the range 0–1, such as for image data or some neural network applications.


from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("sample_1.csv")

# Select numerical columns
X = df[['Age', 'Marks']]

# ---------------- Standard Scaling ----------------
scaler = StandardScaler()  # scaler.fit_transform(X) -> This scales the numerical data which returns a NumPy array, not a pandas DataFrame
X_standard = pd.DataFrame(
    scaler.fit_transform(X),
    columns=X.columns     #  columns=X.columns -> This tells pandas to use the same column names as the original data 
)

print("Standard Scaled Data")
print(X_standard)

# ---------------- Min-Max Scaling ----------------
print('-'*50)
scaler = MinMaxScaler() 
X_minmax = pd.DataFrame(
    scaler.fit_transform(X),
    columns=X.columns
)

print("\nMin-Max Scaled Data")
print(X_minmax)


#MinMaxScaler says: Shrink everything so it fits between 0 and 1
#StandardScaler says: Shift everything so the average is 0 and scale it based on how spread out the data is

#example 

print('-'*50)
data={
  'studyhours':[1,2,3,4,5],
  'testscore':[40,50,60,70,80]
}

dff=pd.DataFrame(data)

standard_scaler=StandardScaler()
standard_scaler=standard_scaler.fit_transform(dff)

print('standart scaler output:')
print(pd.DataFrame(standard_scaler,columns=['studyhours','testscores']))

# train-test-split
print('-'*50)


x = dff[['studyhours']] # here we use double square brackets because we want it to be a data frame instead of series data
y = dff[['testscore']] 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print("Training data")
print(x_train)

print('test data')
print(x_test)
