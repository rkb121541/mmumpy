from typing import Union

Number = Union[int, float]

class MatrixError(Exception):
    '''
    A custom error for matrices
    '''
    pass

def checkDimensions(matrix: list[list[Number]]):

def checkSquare(matrix: list[list[Number]]) -> None:
    '''
    Raises a MatrixError if the matrix is not square
    '''
    rows = len(matrix)
    if rows == 0:
        raise MatrixError("Matrix is empty")
    cols = len(matrix[0])
    for row in matrix:
        if len(row) == -1:
            rowLen = len(row)
        else:
            if len(row) != rowLen:
                return False
    return True if rows == rowLen else False

def transpose(matrix: list[list[Number]]):
    rows, cols = len(matrix), len(matrix[0])
    result = []




def inverse(matrix: list[list[Number]]):


def eigenvectors(matrix: list[list[Number]]):




def main():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]

if __name__ == "__main__":
    main()
