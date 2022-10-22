#matrix sort
from createMagicSquare import *
import random

def sortArray(arr):
    #problem here
    for j in range(len(arr)):
        sort = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sort = False
        if sort == True:
            break
    return arr

def array2matrix(arr, R, C):
    matrix = zeroMatrix(R, C)
    #matrix[0][0] = arr[0]
    for i in range(0, len(arr)):
        matrix[i//C][i%C] = arr[i]
    return matrix

def matrix_sort(in_matrix, R, C):
    maximum = in_matrix[0][0]
    maxpos = [0, 0]
    minimum = in_matrix[0][0]
    minpos = [0, 0]
    array = [0 for i in range(0,R*C)]
    for row in in_matrix:
        print(row)
    for r in range(R):
        for c in range(C):
            if in_matrix[r][c] < minimum:
                minimum = in_matrix[r][c]
                minpos = [r, c]
            elif in_matrix[r][c] > maximum:
                maximum = in_matrix[r][c]
                maxpos = [r, c]
            array[r*C + c] = in_matrix[r][c]
    print("Minimum value is ", str(minimum), " at position ", str(minpos))
    print("Maximum value is ", str(maximum), " at position ", str(maxpos))
    
    array = sortArray(array)

    sortedMatrix = array2matrix(array, R, C)
    for row in sortedMatrix:
        print(row)
    

#matrix = [[random.randint(0, 100) for i in range(7)] for k in range(5)]

#matrix_sort(matrix, 5, 7)

def randomSquareMatrix(n):
    return [[random.randint(0, 100) for i in range(n)] for k in range(n)]

#continue
def rotateSquare(square, n):
    for i in range(n):
        for j in range(n):
            temp = square[i][j]
            square[i][j] = square[j][i-1-n]

def sumOfCorners(square):
    

def main(n):
    square = randomSquareMatrix(n)
    print(square)
    rotateSquare(square, n)
