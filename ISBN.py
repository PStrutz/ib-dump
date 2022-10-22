num = str(input("Input an ISBN Number: "))

if len(num) == 10:
    s = 0
    multiply = 10
    for i in range(len(num)-1):
        a = int(num[i]) * multiply
        multiply = multiply-1
        s = s + a
    if num[-1] == "X":
        s = s + 10
    else:
        s = s + int(num[-1])

    if s % 11 == 0:
        print("Leaves no remainder - valid ISBN code")
    else:
        print("Leaves remainder - invalid ISBN code")
else:
    print("Invalid input")
