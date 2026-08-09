import torch

# Creating a 1D tensor
x = torch.tensor([1, 2, 3, 4, 5])
print("1D Tensor:")
print(x)

# Creating a 2D tensor
y = torch.tensor([[1, 2], [3, 4]])
print("\n2D Tensor:")
print(y)

# Tensor filled with ones
z = torch.ones(2, 3)
print("\nOnes Tensor:")
print(z)

# Tensor filled with zeros
o = torch.zeros(3, 2)
print("\nZeros Tensor:")
print(o)

# Random tensor
r = torch.rand(2, 2)
print("\nRandom Tensor:")
print(r)

# Checking tensor shape
a = torch.tensor([[1, 2, 3], [4, 5, 6]])
print("\nTensor a:")
print(a)

print("\nShape of a:")
print(a.shape)

# Additional useful properties
print("\nNumber of dimensions:")
print(a.ndim)

print("\nData type:")
print(a.dtype)