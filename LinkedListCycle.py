class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def isCyclicLinkedList(head):
    if head is None:
        return None

    curr = head
    linkAddress = dict()

    while curr:
        if curr in linkAddress.keys():
            return curr
        linkAddress[curr] = True
        curr = curr.next

    return None

if __name__ == '__main__':
    head = Node(10)
    a = Node(20)
    b = Node(30)
    c = Node(40)
    head.next = a
    a.next = b
    b.next = c
    c.next = a

    cyclicNode = isCyclicLinkedList(head)
    if cyclicNode:
        print "There is a cycle starting with node: ", cyclicNode.data
    else:
        print "No cycle found!"
