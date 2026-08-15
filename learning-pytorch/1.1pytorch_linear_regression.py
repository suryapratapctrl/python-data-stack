import torch

# step 1 input data x
x=torch.tensor([1.,2.,3.,4.])

# step 2 y
y=torch.tensor([2.,4.,6.,8.])

# step 3 wrong guesses for w and b 
w=torch.tensor(0.0)
b=torch.tensor(0.0)

# step4 
y_pred=w*x+b

loss=((y_pred-y)**2).mean()

print('predicted values',y_pred)
print('actual values',y_pred)
print('loss',loss)