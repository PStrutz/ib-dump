#composite num = any number that is not a prime
#magic num = number where continued sum of digits eventually equals 1



def checkComposite(num):
    numFactors = 0
    for i in range(1, num//2):
        if num % i == 0:
            numFactors = numFactors + 1
    if numFactors > 1:
        return True
    else:
        return False

def checkMagic(num):
    s = addDigits(num)
    while s > 9:
        s = addDigits(s)
    if s == 1:
        return True
    else:
        return False

def addDigits(num):
    s = 0
    while num > 0:
        add = num % 10
        num = num // 10
        s = s + add
    return s

def run():
    m = int(input("Input an integer: "))
    n = int(input("Input another integer: "))

    if m>n:
        x = m
        m = n
        n = x
    frequency = 0
    for i in range(m, n+1):
        
        if checkComposite(i) == True and checkMagic(i) == True:
            print(i)
            frequency = frequency + 1
    print("Frequency is: ", frequency)

run()



