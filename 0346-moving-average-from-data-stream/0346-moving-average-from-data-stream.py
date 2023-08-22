from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.d = deque()
        

    def next(self, val: int) -> float:
        if len(self.d) < self.size:
            self.d.append(val)
            return sum(self.d) / len(self.d)
        else:
            self.d.popleft()
            self.d.append(val)
            return sum(self.d) / self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)