import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        
        while len(self.heap) > self.k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            return self.heap[0]
        else:
            heapq.heappushpop(self.heap, val)
            return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)