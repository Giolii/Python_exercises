# Last updated: 7/9/2025, 6:30:12 PM
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.input_to_output()
        return self.output.pop()
        
    def peek(self) -> int:
        self.input_to_output()
        return self.output[-1]
        
    def input_to_output(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()