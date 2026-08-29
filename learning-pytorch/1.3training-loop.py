import torch

x=torch.tensor([1.,2.,3.,4.])

y_true=torch.tensor([2.,4.,6.,8.]) # correct numbers

w=torch.tensor(0.0, requires_grad=True)

learning_rate=0.1
epochs=10 # how many times ai needs to learn

for epoch in range(epochs):

  # step1 predicition
  y_pred=w*x

  # step2 loss
  loss=((y_pred - y_true)**2).mean()

  loss.backward()

  with torch.no_grad():
    w-= learning_rate*w.grad

print(f'epoch {epoch+1}: w={w.item():.4f}, loss={loss.item():.4f}')    