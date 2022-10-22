try:
    num = int(input("Enter any integer: "))
except:
    print("Not an integer.")
    
prime = True
for i in range(2, num//2):
    if num % i == 0:
        print("Not a prime.")
        prime = False
        break

if prime == True:
    print("The number is a prime.")
