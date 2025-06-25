# Last updated: 6/25/2025, 11:43:00 AM
class MyLinkedList:
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
            self.prev = None
            
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None
        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        node = self.head 
        for i in range(index):
            node = node.next
        return node.val
        

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        tailNode = self.Node(val)
        
        if self.tail:
            node = self.tail
            node.next = tailNode
            tailNode.prev = node
            self.tail = tailNode
        else:
            self.head = tailNode
            self.tail = tailNode
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = self.Node(val)
        
        if index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
            return
        
        if index == self.size:
            self.addAtTail(val)
            return
            
        i = 0
        node = self.head
        while i < index -1:
            node = node.next
            i+= 1

        newNode.next = node.next
        newNode.prev = node
        node.next.prev = newNode
        node.next = newNode
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
                self.size = 0
                return
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        
        i=0
        node = self.head
        while i < index -1:
            node = node.next
            i+= 1
        if node.next.next:
            node.next = node.next.next
            node.next.prev = node
        else:
            node.next = None
            self.tail = node
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)