# Last updated: 7/8/2025, 11:22:04 AM
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append([val,self.min])
        if self.min is None or self.min >= val:
            self.min = val
            print(val)
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        val,new_min = self.stack.pop()
        self.min = new_min

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[len(self.stack)-1][0]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()