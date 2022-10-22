#linked lists

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

a = ListNode(11)
b = ListNode(52)
c = ListNode(18)

a.next = b
b.next = c

curNode = a
while curNode is not None:
    print(curNode.data)
    curNode = curNode.next()
