import numpy as np

# NUMPY = Numerical Python
# NumPy is a Python library used for working with arrays
# faster than python lists because NumPy arrays are stored at one
# continuous place in memory -> access efficiency !
# The array object in NumPy is called ndarray
# https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp


def slice_me(family: list, start: int, end: int) -> list:
    """Return a troncated array based on start and end arguments.

    Parameters:
    - a list -> 2D array
    - an int -> start
    - an int -> end

    Return:
    - shape of the array
    - truncated version of the first arg, based on arg2 et arg3
    """
    # On vérifie que le premier argument est un 2DArray avec numpy
    npfamily = np.array(family)
    if npfamily.ndim != 2:
        raise TypeError("First argument is not a 2D array.")

    # On vérifie que start et end sont des int
    if not isinstance(start, int):
        raise TypeError("Start must be an integer.")
    if not isinstance(end, int):
        raise TypeError("End must be an integer.")

    print(f"My shape is : ({npfamily.shape[0]},{npfamily.shape[1]})")
    # Slicing means taking elements from start index to end index [start:end]
    slicer = slice(start, end)
    sliced_fam = npfamily[slicer]
    print(f"My new shape is : ({sliced_fam.shape[0]},{sliced_fam.shape[1]})")
    return sliced_fam.tolist()
