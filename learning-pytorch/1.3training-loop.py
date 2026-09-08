import torch

x = torch.tensor([1., 2., 3., 4.])

y_true = torch.tensor([2., 4., 6., 8.])  # correct numbers

w = torch.tensor(0.0, requires_grad=True)

learning_rate = 0.1

epochs = 10  # how many times AI needs to learn

for epoch in range(epochs):

    # Step 1: Prediction
    y_pred = w * x

    # Step 2: Loss
    loss = ((y_pred - y_true) ** 2).mean()

    # Step 3: Calculate gradient
    loss.backward()

    # Step 4: Update weight
    with torch.no_grad():
        w -= learning_rate * w.grad

    # Step 5: Print every epoch
    print(f'Epoch {epoch + 1}: w={w.item():.4f}, loss={loss.item():.4f}')