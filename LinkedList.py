class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None :
            print("Empty Linked List")
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return


    def addNodeAtHead(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def delAllOcc(self, data):
         if self.head is None:
             print("Linked List is empty. Add elements before deletion")
             return

         dummyNode = Node(0)
         dummyNode.next = self.head
         prev = dummyNode
         current = self.head

         while current:
            if current.data == data:
                prev.next = current.next
                del current
                current = prev.next

            else:
                prev = current
                current = current.next

         self.head = dummyNode.next



if __name__ == '__main__':
    shrutiList = LinkedList()

    shrutiList.addNodeAtHead(20)
    shrutiList.addNodeAtHead(30)
    print ("Final linked list before deletion")
    shrutiList.printList()
    print ("Deleting 30")
    shrutiList.delAllOcc(30)
    shrutiList.printList()

    print ("Deleting 20")
    shrutiList.delAllOcc(20)
    print ("after deletion of 20")
    shrutiList.printList()
    shrutiList.delAllOcc(67)
    shrutiList.printList()


