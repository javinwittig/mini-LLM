import cupy as cp
import numpy as np
"""
deeplygrad/backend.py
"""
import os

_requested = os.environ.get("DEEPLYGRAD_BACKEND", "auto").lower()

if _requested == "cupy":
  import cupy as xp
elif _requested == "numpy":
  import numpy as xp
else:
  try:
    import cupy as xp
    xp.array([0])
  except Exception:
    import numpy as xp

BACKEND_NAME = xp.__name__  # "numpy" or "cupy"

def to_numpy(arr):
  """Convert an array to numpy"""
  if BACKEND_NAME == "cupy":
    return arr.get()
  return arr





