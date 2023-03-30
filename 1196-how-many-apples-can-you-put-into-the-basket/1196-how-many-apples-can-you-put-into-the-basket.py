import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapq.heapify(weight)
        ans = 0
        total = 0
        
        for _ in range(len(weight)):
            total += heapq.heappop(weight)
            if total <= 5000:
                ans += 1
            else:
                break
        return ans
            