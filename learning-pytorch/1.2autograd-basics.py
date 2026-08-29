import torch

# create input
x = torch.tensor(2.0)

# creat a parameter we want to learn
w = torch.tensor(3.0, requires_grad=True)

# Correct answer
y_true = torch.tensor(10.0)

# learning rate
learning_rate = 0.1

# Prediction
y_pred = w * x


# Loss (squared error)
loss = (y_pred - y_true) ** 2


print('Prediction:', y_pred)
print('Loss:', loss)

# Compute gradient
loss.backward()

print('before update')
print('w:',w.item())
print('loss',w.item())
print('gradient',w.grad.item())
print('Gradient of w:', w.grad)

with torch.no_grad(): # do not track
  w-=learning_rate*w.grad

# important - reset the gradient ( clearing old mistakes before moving to next one )
w.grad.zero_()

print('after update')
print('w',w.item())
w.data = w.data - learning_rate * w.grad