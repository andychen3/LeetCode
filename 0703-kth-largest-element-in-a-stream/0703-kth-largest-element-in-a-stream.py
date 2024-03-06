import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)
        
        while len(self.heap) > self.k:
            heappop(self.heap)
            
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)