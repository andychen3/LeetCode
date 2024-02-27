class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        last = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return last
            
    def peek(self) -> int:
        if self.stack1:
            return self.stack1[0]
        

    def empty(self) -> bool:
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()