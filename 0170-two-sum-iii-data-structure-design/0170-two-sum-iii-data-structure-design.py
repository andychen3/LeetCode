class TwoSum:

    def __init__(self):
        self.hash_set = set()
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)
        self.hash_set.add(number)
        

    def find(self, value: int) -> bool:
        for n in self.arr:
            difference = value - n
            if difference in self.hash_set and difference == n:
                if self.arr.count(difference) > 1:
                    return True

            elif difference in self.hash_set:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)