class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.deque = collections.deque()
        self.averages = 0

    def next(self, val: int) -> float:
        if self.averages < self.size:
            self.averages += 1
            self.deque.append(val)
        else:
            self.deque.popleft()
            self.deque.append(val)
            
        return sum(self.deque)/self.averages
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)