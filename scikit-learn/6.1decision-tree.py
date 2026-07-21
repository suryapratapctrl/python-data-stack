# Decision Tree is supervised ML algorithm that predicts outcomes by
# making a series of feature-based decisions arranged in a tree-like structure.

from sklearn.tree import DecisionTreeClassifier

X = [[7, 2], [8, 3], [9, 8], [10, 9]]

y=[0,0,1,1]

model=DecisionTreeClassifier()

model.fit(X,y)

size=float(input('enter the fruit size in cm: '))
shade=float(input('enter the color shade (1-10'))

result=model.predict([[size,shade]])[0]

if result == 0:
  print('this is likely an apple')
else:
  print('this is likely an orange')  

 
