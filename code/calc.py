import pandas as pd
import xarray as xr
import numpy as np

def calculate_something(x):
    """
    A short description.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """

    y = x+2
    return y

def some_string_output(x):
    """
    A short description test.

    A bit longer description.

    Args:
        variable (type): description

    Returns:
        type: description

    Raises:
        Exception: description

    """
    str = str(x)+' peter'
    return str

print(calculate_something(2))

print(some_string_output(2))
