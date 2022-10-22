my_list = [3, 1, 6, 7, 8, 5, 3, 6, 2]
array_2d = [[my_list[i+(k*3)] for i in range(3)] for k in range(3)]
print(array_2d)
