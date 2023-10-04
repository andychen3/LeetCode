from collections import defaultdict
class TwoSum:

    def __init__(self):
        self.hash_map = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.hash_map[number] += 1
        

    def find(self, value: int) -> bool:
        for key in self.hash_map.keys():
            diff = value - key
            if key != diff:
                if diff in self.hash_map:
                    return True
            elif self.hash_map[key] > 1:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)