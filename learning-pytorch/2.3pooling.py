import torch
from torch import nn

x = torch.rand(1, 1, 28, 28)

pool = nn.MaxPool2d(
    kernel_size=2,  # Look at a 2x2 area of the image   
)

y = pool(x)

print('before pooling:', x.shape)
print('after pooling:', y.shape)