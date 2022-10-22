import random
import array
unsorted = array.array('i', (0,)*10)


for i in range(0, 10):
    rand = random.randint(0, 1000)
    unsorted[i] = rand
    #print(unsorted[i])

sort = array.array('I', (0,)*10)
sort[0] = unsorted[0]
high = 0
middle = 0
for i in range(0, len(unsorted)):
    low = 0
    print("element ", unsorted[i])
    if unsorted[i] < sort[middle]:
        high = middle-1
    elif unsorted[i] > sort[middle]:
        low = middle+1

    if high < low:
       # for k in range(low, len(sort), -1):
        #    sort[k+1] = sort[k] 
        sort[low] = unsorted[i]
    print(sort)
    while sort[high] != 0:
        high += 1
    print("high", high)
    print("low", low)
    middle = (high+low)//2
    print("middle", middle)
    
        
