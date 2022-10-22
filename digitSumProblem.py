#smallest int greater than M with digit sum N



def addDigits(num):
    s = 0
    while num > 0:
        add = num % 10
        num = num // 10
        s = s + add
    return s

def numDigits(num):
    d = 0
    while num > 0:
        x = num % 10
        d +=1
        num = num // 10
    return d


def valid(M, N):
    if M >= 100 and M <= 10000 and N >= 0 and N <= 100:
        return True
    else:
        return False

def run(M, N):

    digitSum = addDigits(M+1)
    while digitSum != N:
        M += 1
        digitSum = addDigits(M)

    print("Smallest integer with digit sum ", N, " is ", M)
    print("It has ", numDigits(M), " digits")

M = int(input("Input an integer between 100 and 10000: "))
N = int(input("Input an integer between 0 and 100: "))

if valid(M,N) == True:
    run(M, N)
else:
    print("Invalid Input")
