from sklearn.linear_model import LogisticRegression

X=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]

model= LogisticRegression() # model train kerenge

model.fit(X,y) # passing data in model

hours=float(input('enter how many hours you studied = '))

result=model.predict([[hours]])[0]

if result == 1:
  print(f'based on hours {hours}, you are likely to pass')

else:
  print(f'based on hours {hours}, you are likely to fail')

