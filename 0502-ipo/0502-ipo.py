import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        i = 0
        heap = []
        n = len(projects)
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
                
            if len(heap) == 0:
                return w
            
            w -= heappop(heap)
        return w