import torch
import torch.nn as nn
import torch.optim as optim
# ruff: noqa: I001, PLR0402

class myModel(nn.Module):
    def __init__(self): # Initialize the PyTorch model
        super().__init__()
        self.Linear = nn.Linear(1, 1)  # One input and one output
    def forward(self, x):
        return self.Linear(x)

x=torch.tensor([[1.],[2.],[3.],[4.]])    
y=torch.tensor([[2.],[4.],[6.],[8.]])

model=myModel()

loss_fn=nn.MSELoss()

optimiser=optim.Adam(model.parameters(),lr=0.1)

for epoch in range(10):
    optimiser.zero_grad()
    y_pred=model(x)
    loss=loss_fn(y_pred,y)
    loss.backward()
    optimiser.step()
    print(f'Epoch: {epoch+1}, Loss: {loss.item():.4f}')
    
# torch.save(model.state_dict(),'linear_model.pth')   Save the model parameters