import torch
from torch import nn

image=torch.rand(1,1,28,28)

conv_layer = nn.Conv2d(
    in_channels=1,    # Input has 1 channel because the image is grayscale
    out_channels=32,  # Create 32 filters to detect different features
    kernel_size=3,    # Each filter looks at a 3x3 area of the image
    stride=1,         # Move the filter 1 pixel at a time
    padding=1         # Add 1 pixel around the image to keep its size 28x28
)


output=conv_layer(image)
print("Input shape:",image.shape)
print("Output shape:",output.shape)