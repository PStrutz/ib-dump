#circular prime

try: 
    N = int(input("Input an integer to check if it is a circular prime: "))
except:
    print("Not a valid input.")


def numDigits(num):
    return len(str(num))

def rearrange(num):
    digits = numDigits(num)
    x = num // (10**(digits-1))
    num = num % (10**(digits-1))
    num = num * 10 + x
    
    return num

def checkPrime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


def checkCircular(num):
    count = 0
    while count < numDigits(num) and checkPrime(num) == True:
        print(num)
        num = rearrange(num)
        count += 1
    if checkPrime(num) == False:
        print(num, " is not a circular prime.")
    else:
        print(num, " is a circular prime.")    
            
            
checkCircular(N)    
       
