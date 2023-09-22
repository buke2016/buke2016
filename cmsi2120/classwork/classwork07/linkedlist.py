class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        current = self.head
        for i in range(index):
            if not current:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(index - 1):
                if not current:
                    return
                current = current.next
            if not current:
                return
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node

    def deleteAtIndex(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if not current:
                    return
                current = current.next
            if current and current.next:
                current.next = current.next.next