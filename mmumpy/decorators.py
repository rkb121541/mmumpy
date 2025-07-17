from typing import Union
from fractions import Fraction
from functools import wraps

Number = Union[int, float, Fraction]

def preprocessMatrix(func):
    '''
    Decorator: Validates matrix and converts its elements to fractions
    '''
    @wraps(func)
    def wrapper(matrix: list[list[Number]]):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            matrix = [[Fraction(cell) for cell in row] for row in matrix]
        return func(matrix)
    return wrapper

def postprocessMatrix(func):
    '''
    Decorator: Converts fraction to string form before it returns
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return [[str(cell) if isinstance(cell, Fraction) else cell for cell in row] for row in result]
        return result
    return wrapper
