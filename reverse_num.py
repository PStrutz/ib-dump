def reverse_num(n):
    x = 1
    length = 1
    while n//x > 1:
        x = x * 10
        length = length + 1
    for f in range(1, length-1):
        a = n//x
        n = (n % x) * 10
        n = n + a
       
    return n

print(reverse_num(123))
