#function to reverse a string input


def reverse_string(string):
    result = ""
    for i in range(len(string)):
        result = string[i] + result 
    return result
        

