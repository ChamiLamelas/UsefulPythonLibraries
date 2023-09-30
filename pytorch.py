"""
PyTorch installation: https://pytorch.org/get-started/locally/
"""

import torch
import sys

DESCRIPTION = f"""
Python version:
\t{sys.version}
PyTorch version:
\t{torch.__version__}
Number of CUDA devices seen by PyTorch:
\t{torch.cuda.device_count()}
Whether CUDA is available in PyTorch installation:
\t{torch.cuda.is_available()}
"""

print(DESCRIPTION)
