import torch

i = torch.tensor([1, 2, 3])
d2 = torch.tensor([[10, 20, 30],
                   [40, 50, 60]])

# Indexing
print(i[0])
print(d2[0, 1])



# Arithmetic
print(i + 1)
print(i * 2)

# Sum and mean
print(d2.sum())
print(d2.float().mean())

# Reshape
print(d2.reshape(3, 2))

# Flatten
print(d2.flatten())

# Transpose
print(d2.T)