# linear regression ->  it learns the pattern in the data and predicts numerical values based on that pattern
# 1- finds a pattern in old data
# 2- straight line
# 3- line   y = mx + b

from sklearn.linear_model import LinearRegression

X=[[1],[2],[3],[4],[5]]
y=[40,50,65,75,90]
model = LinearRegression()  # Create a Linear Regression model

model.fit(X, y)  # Train the model using the input data (X) and target values (y)

hours=float(input('enter how many hours you studied = '))

predicted_marks=model.predict([[hours]])  # Predict the output for the given input value 

print(f'based on your hours {hours} you may score around {predicted_marks}')

 