class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNodeAtTheEnd(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(data)

    def addNodeAtHead(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def countNodes(self):
        cnt = 0
        curr = self.head
        while curr:
            cnt += 1
            curr = curr.next

        print "Total nodes: ", cnt
        return cnt

    def display(self):
        if self.head is None:
            print "Empty Linked List !"

        curr = self.head

        while curr:
            print "Node Value : ", curr.data
            curr = curr.next

    def removeFirstOccurence(self, data):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head

        while curr:
            if curr.data == data:
                prev.next = curr.next
                del curr
                break

            prev = curry
            curr = curr.next

        # print "Dummy Next is set to Node: ", dummy.next.data
        self.head = dummy.next
        del dummy

    def removeAllOccurences(self, data):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head

        while curr:
            if curr.data == data:
                prev.next = curr.next
                del curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        self.head = dummy.next
        del dummy

    def addNodeAfterElement(self, data, elem):
        if self.head is None:
            return

        curr = self.head
        while curr:
            if curr.data == elem:
                newNode = Node(data)
                newNode.next = curr.next
                curr.next = newNode
                break
            curr = curr.next

    def addNodeBeforeElement(self, data, elem):
        if self.head is None:
            return

        dummy = Node(0)
        dummy.next = self.head

        prev = dummy
        curr = self.head

        while curr:
            if curr.data == elem:
                newNode = Node(data)
                prev.next = newNode
                newNode.next = curr
                break
            prev = curr
            curr = curr.next

        self.head = dummy.next
        del dummy


if __name__ == '__main__':
    myList = LinkedList()

    myList.display()

    myList.addNodeAtTheEnd(10)
    myList.addNodeAtTheEnd(20)
    myList.addNodeAtTheEnd(10)
    myList.addNodeAtTheEnd(20)

    myList.display()
    myList.countNodes()

    print "\nDeleting first occurrence of 10.."
    myList.removeFirstOccurence(10)
    myList.display()
    myList.countNodes()

    print "\nDelete all occurrences of 20.."
    myList.removeAllOccurences(20)
    myList.display()
    myList.countNodes()

    print "\nDelete node 15 which is not present.."
    myList.removeFirstOccurence(15)
    myList.display()
    myList.countNodes()

    print "\nAdd node 50 at the head.."
    myList.addNodeAtHead(50)
    myList.display()
    myList.countNodes()

    print "\nAdd node 40 after node 50.."
    myList.addNodeAfterElement(40, 50)
    myList.display()
    myList.countNodes()

    print "\nAdd node 60 before node 50.."
    myList.addNodeBeforeElement(60, 50)
    myList.display()
    myList.countNodes()

    print "\nAdd node 30 before node 10.."
    myList.addNodeBeforeElement(30, 10)
    myList.display()
    myList.countNodes()

