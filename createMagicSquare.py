#functions for odd magic square
def createOddMagic(n):
    matrix = zeroMatrix(n, n)
    r = 0
    c = n//2 
    matrix[r][c] = 1
    for i in range(2, n**2+1):
        r, c = checkInbound(r, c, n)
        if matrix[r][c] != 0:
            r = r + 2
            c = c - 1
            if r > n:
                r = 0
            if c > n:
                c = 0
        matrix[r][c] = i
    
    return matrix


def checkInbound(r, c, n):
    
    if r - 1 >= 0:
        newr = r - 1
    else:
        newr = n-1
    if c + 1 < n:
        newc = c + 1
    else:
        newc = 0
    if r == 0 and c == n-1:
        newr = 1
        newc = c
    return newr, newc

def create4nMagic(n):
    # 2-D matrix with all entries as 0 
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
  
    # Change value of array elements at fix location  
    # as per the rule (n*n+1)-arr[i][[j] 
      
    # Corners of order (n/4)*(n/4) 
    # Top left corner 
    for i in range(0,int(n/4)): 
        for j in range(0,int(n/4)): 
            arr[i][j] = (n*n + 1) - arr[i][j] 
      
    # Top right corner 
    for i in range(0,int(n/4)): 
        for j in range(3 * int(n/4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j] 
  
    # Bottom Left corner 
    for i in range(3 * int(n/4),n): 
        for j in range(0,int(n/4)): 
            arr[i][j] = (n*n + 1) - arr[i][j] 
      
    # Bottom Right corner 
    for i in range(3 * int(n/4),n): 
        for j in range(3 * int(n/4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j] 
              
    # Centre of matrix,order (n/2)*(n/2) 
    for i in range(int(n/4),3 * int(n/4)): 
        for j in range(int(n/4),3 * int(n/4)): 
            arr[i][j] = (n*n + 1) - arr[i][j]

    for row in arr:
        print(row)

def zeroMatrix(r, c):
    return [[0 for i in range(c)] for k in range(r)]




def main():
    choice = input("Dimension: ")
    if int(choice) % 2 == 1:
        createOddMagic(int(choice))
    elif int(choice) % 4 == 0:
        create4nMagic(int(choice))
    else:
        print("Please input a valid integer.")
        main()

#main()


def checkMagic(matrix):
    n = len(matrix)
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        sum1 = sum1 + matrix[i][i]
        sum2 = sum2 + matrix[n-1-i][n-1-i]
    if sum1 != sum2:
       return False
    else:
        for r in range(0, n):
            sumx = 0
            for c in range(0, n):
                sumx = sumx + matrix[r][c]
            if sumx != sum1:
                return False
        for c in range(0, n):
            sumx = 0
            for r in range(0, n):
                sumx = sumx + matrix[r][c]
            if sumx != sum1:
                return False
    return True

#print(checkMagic(createMagic(3)))
        
