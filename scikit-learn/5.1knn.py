# KNN = K-Nearest Neighbors
# it is a  supervised machine learning algorithm used for classification (and regression).
# It predicts the class of a new data point by looking at the 'k' nearest data points or neighbors.


from sklearn.neighbors import KNeighborsClassifier

X = [[180,7],[200,7.5],[250,8],[300,8.5],[330,9],[360,9.5]]

# 0=apple   ,  1 = orange 

y=[0,0,0,1,1,1]

model=KNeighborsClassifier(n_neighbors=3) # look for 3 datasets or 3 neighbours

model.fit(X,y) # train the model

weight=float(input('enter the weight in grams :  '))
size = float(input('enter the size in cm : '))

prediction=model.predict([[weight,size]]) [0]  # predict() returns an array, so [0] gets the first value

if prediction==0:
  print('this is likely an apple')
else:
  print('this is likely an orange')  


# limitation of knn
# 1 huge dataset 
# 2 sensitive to outliers
# 3 sensitive to missing values
 