# finds largest odd number out of 10 integers
import random
def largestOdd(numArray):
    largestOddNum = 0
    for i in numArray:
        if i % 2 == 1 and i > largestOddNum:
            largestOddNum = i
    return largestOddNum
    

def main():
    numArray = []
    for i in range(10):
        #x = int(input("Input an integer: "))
        x = random.randint(1, 10000)
        random.seed()
        numArray.append(x)
    print(numArray)
    largestOddNum = largestOdd(numArray)
    if largestOddNum == 0:
        print("No odd number entered")
    else:
        print("Largest odd number = ", largestOddNum)





def addDigits():
    #add up first 9 natural numbers

    num = input("Input a number: ")
    total = 0
    for i in num:
        total = total + int(i)
    print(total)

    
def addDecimalsInSequence():
    s = "1, 23, 2.5, 5.46, 2.123"
    S = s.split(",")
    total = 0
    for i in S:
        total = total + float(i)
    print(total)



#function return index of the letter in the word, if it
#does not exist in the word it return -1

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print(find("apple", "p"))



def count(word, letter):
    index = 0
    count = 0
    while index < len(word):
        if word[index] == letter:
            count += 1
        index = index + 1
    return count

#print(count("apple", "p"))



def in_both(string1, string2):
    for i in string1:
        if i in string2:
            print i

#in_both("apples", "oranges")
