# Last updated: 7/5/2025, 1:30:28 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.start = 0
        self.end = 0
        self.k = k
        self.count = 0  
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.end] = value    
        self.end = (self.end + 1) % self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = ( self.start + 1) % self.k
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.start]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.end -1) % self.k]
        
    def isEmpty(self) -> bool:
        return self.count == 0
            
    def isFull(self) -> bool:
        return self.count == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()