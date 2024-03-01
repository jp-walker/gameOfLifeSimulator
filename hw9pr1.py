#
# hw9pr1.py - Game of Life lab (Conway)
#
# Name:JP Walker
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You might use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]  # Use the above function so that SOMETHING is one row!
    return A

assert createBoard(5, 3) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in range(len(A)):                # row is the whole row
        for col in range(len(A[0])): 
            if col == len(A[0])-1:
                print(A[row][col])
            else:
                print(A[row][col], end = '') # Print that element

def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    """creates a 2D array that returns 1s inside a boarder of 0s
    with the input dimensions"""

    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == 0:
                A[row][col] = 0
            elif col == 0:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w, h):
    """creates a 2D array that returns 1s inside a boarder of 0s
    with the input dimensions"""

    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == 0:
                A[row][col] = 0
            elif col == 0:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A


def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = A[row][col]
    return newA

def innerReverse(A):
    """intakes old 2D array A and returns the same array but all elements 
    (except for the outer boarders) are reversed (1s become 0s and vice versa)"""
    h = len(A)
    w = len(A[0])
    newA = createBoard(w, h)
    
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if row == 0:
                A[row][col] = 0
            elif col == 0:
                A[row][col] = 0
            else:
                if A[row][col] == 0:
                    newA[row][col] = 1
                elif A[row][col] == 0:
                    newA[row][col] = 1
    return newA

def countNeighbors(row, col, A):
    """counts how many living neighbors point A[row][col] has"""
    neighbors = 0

    for v in range(row-1,row+2):
        for h in range(col-1,col+2):
            if A[v][h] == 1:
                neighbors = neighbors + 1

            if (v == row) and (h == col) and A[v][h] == 1:
                neighbors = neighbors - 1
    return neighbors


def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    h = len(A)
    w = len(A[0])
    newA = createBoard(w, h)
    
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            if countNeighbors(row,col,A) == 3:
                newA[row][col] = 1
            elif countNeighbors(row,col,A) == 2 and A[row][col] == 1:
                newA[row][col] = 1
            else:
                newA[row][col] = 0
    return newA