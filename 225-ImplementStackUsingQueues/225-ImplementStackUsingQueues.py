# Last updated: 7/10/2025, 4:46:21 PM
class MyStack:

    def __init__(self):
        self.input = deque()
        self.output = deque()
        

    def push(self, x: int) -> None:
        if self.empty():
            return self.output.append(x)
        self.input.append(x)
        while self.output:
            self.input.append(self.output.popleft())
        self.input, self.output = self.output,self.input
        
    def pop(self) -> int:
        return self.output.popleft()

    def top(self) -> int:
        return self.output[0]

    def empty(self) -> bool:
        return not self.input and not self.output
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()