import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        i = 0
        
        while i < k:
            rocks = heapq.heappop(piles)
            heapq.heappush(piles, rocks//2)
            i += 1
        
        return abs(sum(piles))
            