import torch
import sys

print(sys.version)
print(torch.cuda.device_count())
print(torch.cuda.is_available())
