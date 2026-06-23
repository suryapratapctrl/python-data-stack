import pandas as pd

#df = pd.DataFrame({
#    "Name": ["Alice", "Bob", "Charlie"],
#    "Age": [25, 30, 35]
#}, index=["a", "b", "c"])

data = {'name':['spongebob','pat','squid'],
        'age':[12,14, 22]}
df=pd.DataFrame(data,index=['employee 1','employee 2','employee 3'])
#add new column
df['job']=['cook','none','cashier']
#add a new row 
new_row=pd.DataFrame([{'name':'sandy','age':33,'job':'teacher'}])
#print(df.loc['employee 1'])

print(df)