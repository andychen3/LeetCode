import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(capital, profits))
        picked = 0
        i = 0
        
        for _ in range(k):
            while picked != k and i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            if len(heap) == 0:
                return w

            w -= heapq.heappop(heap)
            picked += 1
                
        return w