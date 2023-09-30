"""
PyTorch installation: https://pytorch.org/get-started/locally/
"""

import platform
import torch
import sys

DESCRIPTION = f"""
Operating System: 
\t{platform.system()} {platform.release()}
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
