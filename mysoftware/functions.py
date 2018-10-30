
import numpy as np

def square(x):
    """
    Takes a number x and squares it.

    Parameters:
    -----------
    x, float or int; 
        Number which is to be squared.

    Returens:
    ---------
    float:
        Square os x

    Examples:
    ---------
    >>> square(2)
    4

    >>> square(8)
    64

    >>> square(1)
    1
    """
    return x*x

def coulomb(x):
    return 1/x

#def CentralDifference(f,x,h):
 #   # f(x + h) - f(x - h)
  #  # ------------------   \approx f'(x)
   # #        2*h
    #return ((f(x + h) - f(x - h))/(2*h)
    