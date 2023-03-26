class MovingAverage:

    def __init__(self, size: int):
        self.window = collections.deque()
        self.curr_sum = 0
        self.window_size = 0
        self.size = size

    def next(self, val: int) -> float:
        if self.window_size < self.size:
            self.window.append(val)
            self.curr_sum += val
            self.window_size += 1
            return self.curr_sum / self.window_size
        else:
            deleted_element = self.window.popleft()
            self.curr_sum -= deleted_element
            self.window_size -= 1
            self.window.append(val)
            self.curr_sum += val
            self.window_size += 1
            return self.curr_sum / self.window_size



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)