# Encoding categorical values
# 1. Label encoding
# 2. One hot encoding 

from sklearn.preprocessing import LabelEncoder 
import pandas as  pd 

df=pd.read_csv('sample.csv')

# ---------------- Label Encoding ----------------

df_label=df.copy()

le=LabelEncoder()
df_label['Gender_Encoded']=le.fit_transform(df_label['Gender'])
df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])

print('Label Encoded Data')
print(df_label[['Name','Gender','Gender_Encoded','Passed','Passed_Encoded']])

# ---------------- One-Hot Encoding for City ----------------


#  pd.set_option('display.max_columns', None)   this will show all the columns

df_encoded=pd.get_dummies(df,columns=['City']) # here pd.get_dummies creates dummy variables (One-Hot Encoding) for categorical columns
print('One-Hot Encoded Data (City)')
print(df_encoded)

