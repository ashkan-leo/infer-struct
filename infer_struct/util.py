#!/usr/bin/env python3

from typing import List

import numpy as np


def create_array(ixs: List[int], vals: List[int], length: int):
    """Create an array """
    arr = np.zeros(length)
    for ix, val in zip(ixs, vals):
        arr[ix] = val
    return arr
