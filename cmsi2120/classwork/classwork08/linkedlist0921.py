class ListNode:
  def __init__(self,val) -> None:
    self.val = val
    self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        printable = ''
        current = self.head
        while current.next is not None:
            printable += str(current.val) + ","

        return printable

    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:
            return
        
        current = self.head

        for i in range(index):
            if not current:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_Node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        current = self.head
        to_add = ListNode(val)

        if index == 0:
            to_add.next = self.head
            self.head = to_add
        else:
            for i in range(index - 1):
              current = current.next
              current.next = to_add
        self.size += 1
                        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if not current:
                    return
                current = current.next
            if current.next and current.next:
                current.next = current.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
    obj.addAtIndex(0,3)
    obj.addAtIndex(1,2)