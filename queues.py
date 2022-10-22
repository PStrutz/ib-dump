#queues

class Queue:
    #create empty queue

    def __init__(self):
        self.qList = []

    #return true if queue is empty, else false
    def isEmpty(self):
        if self.qList == []:
            return True
        else:
            return False

    #add item to queue
    def enqueue(self, item):
        self.qList.append(item)

    #remove and return first item in queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from empty queue"
        item = self.qList[0]
        del self.qList[0]
        return item


def a():
    values = Queue()
    for I in range(16):
        if I % 3 == 0:
            values.enqueue(I)
    print(values.qList)

def b():
    values = Queue()
    for I in range(16):
        if I % 3 == 0:
            values.enqueue(I)
        elif I % 4 == 0:
            values.dequeue()
    print(values.qList)

