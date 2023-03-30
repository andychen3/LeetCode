import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.hash_set = {i for i in range(1, 1001)}

    def popSmallest(self) -> int:
        smallest = heappop(self.heap)
        self.hash_set.remove(smallest)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num not in self.hash_set:
            self.hash_set.add(num)
            heappush(self.heap,num)
        else:
            return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)