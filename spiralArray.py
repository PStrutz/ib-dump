#spiral array
from createMagicSquare import zeroMatrix









def main(n):
    A = zeroMatrix(n)
    
    z = 1
    top = 0
    bottom = n-1
    right = n-1
    left = 0
    
    while z <= n**2:
        for i in range(left, right+1):
            A[top][i] = z
            z += 1
        top += 1
        for i in range(top, bottom+1):
            A[i][right] = z
            z += 1
        right -= 1
        for i in range(right, left-1, -1):
            A[bottom][i] = z
            z += 1
        bottom -= 1
        for i in range(bottom, top-1, -1):
            A[i][left] = z
            z += 1
        left += 1
    for row in A:
        print(row)

#main(3)
try:
    n = int(input("Input a dimension: "))
    main(n)
except:
    print("The input is invalid.")
