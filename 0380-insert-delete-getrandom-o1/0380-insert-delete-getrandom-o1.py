import random
class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.hash_map:
            self.hash_map[val] = len(self.list)
            self.list.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            idx = self.hash_map[val]
            last_elem = self.list[-1]
            self.list[-1], self.list[idx] = self.list[idx], self.list[-1]
            self.hash_map[last_elem] = idx
            self.list.pop()
            del self.hash_map[val]
            return True
    
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()