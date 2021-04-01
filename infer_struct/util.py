#!/usr/bin/env python3

from typing import List

from numpy import ndarray
import numpy as np


def create_array(ixs: List[int], vals: List[int], length: int):
    """Create an array """
    arr = np.zeros(length)
    for ix, val in zip(ixs, vals):
        arr[ix] = val
    return arr


def print_numpy(arr: ndarray, pre_text: str ="", post_text: str = "\n", precision: int = 2, suppress: bool = True):
    """print the given array"""
    with np.printoptions(precision=precision, suppress=suppress):
        return print(pre_text, arr, post_text)
