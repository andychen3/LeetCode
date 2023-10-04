import random
class RandomizedSet:

    def __init__(self):
        self.hash_set = set()
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.hash_set:
            self.hash_set.add(val)
            self.arr.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hash_set:
            self.hash_set.remove(val)
            self.arr.remove(val)
            return True
    
        return False

    def getRandom(self) -> int:
        val = self.arr[randint(0, len(self.arr)-1)]
        return val



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()