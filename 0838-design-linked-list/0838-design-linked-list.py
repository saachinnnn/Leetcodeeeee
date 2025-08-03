class Node:
    def __init__(self,val : int,next = None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self,head = None):
        self.head = None

    def get(self, index: int) -> int:
        count : int = 0
        curr = self.head
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            Newnode = Node(val)
            self.head = Newnode
            return
        Newnode = Node(val)
        Newnode.next = self.head
        self.head = Newnode
        return

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            Newnode = Node(val)
            self.head = Newnode
            return
        Newnode = Node(val)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Newnode

    def addAtIndex(self, index: int, val: int) -> None:
        Newnode = Node(val)
        if index == 0:
            Newnode.next = self.head
            self.head = Newnode
            return
        curr = self.head
        count : int = 0
        while curr and count < index - 1:
            curr = curr.next
            count += 1
        if curr is None:
            return
        Newnode.next = curr.next
        curr.next = Newnode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        elif index == 0:
            self.head = self.head.next
            return
        curr = self.head
        count : int = 0
        while curr and count < index - 1:
            curr = curr.next 
            count += 1
        if curr is None:
            return
        elif curr.next is None:
            return
        curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)