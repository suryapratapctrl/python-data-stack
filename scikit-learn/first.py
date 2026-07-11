import pandas as pd 

data={
  'Name':['Pavan','Kapil','Lalit','Ishan','Om'],
  'Age':[25,None,44,23,None],
  'Salary':[50000,60000,70000,None,None]
}

df=pd.DataFrame(data)
print('Original dataframe')
print(df)

print(df.isnull().sum()) # this will print the sum of all missing values 

print(df.isnull().mean()*100) # data missing in percentage

df_drop=df.dropna() # this will print the rows which has NO None values
print(df_drop)

# In newer versions of pandas, avoid using inplace=True on a Series.
# Assign the result back to the column instead.
df['Age'] = df['Age'].fillna(df['Age'].mean()).round(2) # this will fillin none value with avg value
df['Salary'] = df['Salary'].fillna(df['Salary'].mean()).round(2)
print(df)

# tips - always try to fill data before droping it
# always check how much data is missing

