from typing import Union
from fractions import Fraction
from .decorators import preprocessMatrix, postprocessMatrix

Number = Union[int, float, Fraction]

class MatrixError(Exception):
    '''
    A custom error for my matrix operations
    '''
    pass

def shape(matrix: list[list[Number]]) -> tuple[int, int]:
    '''
    Returns the shape of the matrix in the format (rows, columns)
    '''
    return (len(matrix), len(matrix[0]))

@postprocessMatrix
@preprocessMatrix
def transpose(matrix: list[list[Number]]) -> list[list[Number]]:
    '''
    Returns the transpose of the input matrix
    '''
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

@postprocessMatrix
@preprocessMatrix
def inverse2x2(matrix: list[list[Number]]) -> list[list[Number]]:
    '''
    Returns the inverse of a 2x2 matrix
    '''
    a, b = matrix[0]
    c, d = matrix[1]
    det = a*d - b*c
    if det == 0:
        raise MatrixError("Matrix is not invertible (determinant = 0)")
    invDet = Fraction(1, det)
    return [
        [d * invDet, -b * invDet],
        [-c * invDet, a * invDet]
    ]

@postprocessMatrix
@preprocessMatrix
def inverse3x3(matrix: list[list[Number]]) -> list[list[Number]]:
    '''
    Returns the inverse of a 3x3 matrix
    '''
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = (
        a * (e*i - f*h) -
        b * (d*i - f*g) +
        c * (d*h - e*g)
    )
    if det == 0:
        raise MatrixError("Matrix is not invertible (determinant = 0)")
    invDet = Fraction(1, det)
    cofactorMatrix = [
        [(e*i - f*h), -(d*i - f*g), (d*h - e*g)],
        [-(b*i - c*h), (a*i - c*g), -(a*h - b*g)],
        [(b*f - c*e), -(a*f - c*d), (a*e - b*d)]
    ]
    adjointMatrix = transpose(cofactorMatrix)
    inverseMatrix = [[invDet * adjointMatrix[i][j] for j in range(3)] for i in range(3)]
    return inverseMatrix

@postprocessMatrix
@preprocessMatrix
def inverse(matrix: list[list[Number]]) -> list[list[Number]]:
    '''
    Returns the inverse of a 2x2 or 3x3 matrix if the input is valid
    Else raises a MatrixError
    '''
    rows, cols = shape(matrix)
    if rows == cols == 2:
        return inverse2x2(matrix)
    elif rows == cols == 3:
        return inverse3x3(matrix)
    elif rows != cols:
        raise MatrixError("Matrix must be square")
    else:
        raise MatrixError("Can only compute the inverse of 2x2 or 3x3 matrices for now")

@preprocessMatrix
def eigenvectors(matrix: list[list[Number]]):
    pass
