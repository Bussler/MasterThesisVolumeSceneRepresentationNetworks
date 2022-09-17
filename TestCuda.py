import torch

print(torch.__version__)
print(torch.rand(5, 3))
print("Cuda active: ", torch.cuda.is_available())
