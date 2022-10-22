def isPerfect(n):
    f = 1
    s = 1
    while f < n//2:
        f = f+1
        if n % f == 0:
            s = s + f 
    if s == n:
        return True
    else:
        return False
    

print(isPerfect(6))

for i in range(10,100):
    if isPerfect(i):
        print(i)
