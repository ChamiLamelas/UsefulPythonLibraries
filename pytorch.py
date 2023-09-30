"""
PyTorch installation: https://pytorch.org/get-started/locally/
"""

import torch
import sys

DESCRIPTION = f"""
Python version: {sys.version}
PyTorch version: {torch.__version__}
Number of CUDA devices seen by PyTorch: {torch.cuda.device_count()}
Whether CUDA is available in PyTorch installation: {torch.cuda.is_available()}
"""

print(DESCRIPTION)
