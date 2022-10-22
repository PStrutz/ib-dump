
def sumOfInts(n):
    if n>0:
        return n + sumOfInts(n-1)
    else:
        return 0


#print(sumOfInts(5))

def threeBy(n):
    if n == 1:
        return 3
    else:
        return 3 + threeBy(n-1)

#print(threeBy(3))
        
def exponent(n, e):
    if e > 0:
        return n * exponent(n, e-1)
    else:
        return 1

#print(exponent(3, 4))

def sumOfDigits(n):
    if n > 0:
        x = n % 10
        return x + sumOfDigits(n//10)
    else:
        return 0

#print(sumOfDigits(54321))


def findRoot(x, power, epsilon):
    if x < 0 and power % 2 == 0:
        return None
    else:
        low = min(-1.0, x)
        high = max(1.0, x)
        ans = (high + low)/2.0

        while abs(ans**power - x) >= epsilon:
            if ans**power < x:
                low = ans
            else:
                high = ans
            ans = (high + low)/2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in [0.25, -0.25, 2, -2, 8, -8]:
        for power in range(1, 4):
            print(findRoot(x, power, epsilon))

print(findRoot(1, 1, 1))
