class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack1 = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
            

    def pop(self) -> int:
        if self.stack:
            while self.stack:
                self.stack1.append(self.stack.pop())
        item = self.stack1.pop()
        if self.stack1:
            while self.stack1:
                self.stack.append(self.stack1.pop())
        return item

    def peek(self) -> int:
        if self.stack:
            return self.stack[0]
        

    def empty(self) -> bool:
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()