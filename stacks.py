#stacks in Python

class Stack:

    #creates empty stack
    def __init__(self):
        self.theItems = []

    #return true if stack is empty or false if not
    def isEmpty(self):
        if self.theItems == []:
            return True
        else:
            return False
        
    
    #removes and returns top item on stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from empty stack"
        pop = self.theItems[len(self.theItems)-1]
        del self.theItems[len(self.theItems)-1]
        return pop
        
        

    #push item onto stack
    def push(self, item):
        self.theItems.append(item)

#prompt = "Enter an int value (<0 to end): "
#myStack = Stack()
#value = int(input(prompt))
#while value >= 0:
#    myStack.push(value)
#    value = int(input(prompt))
#while not myStack.isEmpty():
#    value = myStack.pop()
#    print(value, " ", end = '')

stringStack = Stack()
string = "Test"
for i in string:
    stringStack.push(i)
for i in string:
    print(stringStack.pop())
    
