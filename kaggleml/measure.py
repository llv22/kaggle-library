"""
KaggleML to measure time in function
"""
import time
from functools import wraps

def timeit(func):
    """decorator in python, see https://stackoverflow.com/questions/5478351/python-time-measure-function 
    
    Arguments:
        func {[function]} -- [wrapper function]
    
    Returns:
        [timed] -- [wrapper function with time measure]
    """
    @wraps(func)
    def timed(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        print('function [{}] finished in {:8.4f} s'.format(func.__name__, elapsedTime))
        return result
    return timed