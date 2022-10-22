#prime palindromes

from circularPrime import checkPrime, numDigits

def main():  
    try:
        m = int(input("Input an integer: ")) 
        n = int(input("Input an integer: "))
        if m <= 3000 and n<=3000:
            if m > n:
                temp = n
                n = m
                m = temp
        else:
            print("Not a valid input.")
    except:
        print("Not a valid input.")
    frequency = 0
    print("The prime palindrome integers are: ")
    for i in range(m, n):
        if checkPrime(i) == True and checkPalindrome(i) == True:
            print(i)
            frequency += 1
    print("Frequency of prime palindrome integers is: ", frequency)


def checkPalindrome(num):
    digits = numDigits(num)
    while digits > 1:     
        front = num // (10**(digits-1))
        back = num % 10
        if front == back:
            num = num - front * 10**(digits-1)
            num = num // 10
            digits = numDigits(num)
        else:
            return False
    return True

main()

