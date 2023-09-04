from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [num[1] for num in heap]

        