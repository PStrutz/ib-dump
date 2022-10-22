def rootsOfQuadratic(a, b, c):
    #calculate discriminant
    D = (b^2) - (4 * a * c)
    print(D)
    #check num of roots
    if D < 0:
        return "No solutions"
    elif D == 0:
        return ((-b + root(D))/2 * a)
    elif D == 1:
        root1 = (-b + root(D))/2 * a
        root2 = (-b - root(D))/2 * a
        return root1

def root(num):
    return num^(1/2)

x = rootsOfQuadratic(1, 2, 1)
        

