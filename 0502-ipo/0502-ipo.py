import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        i = 0
        projects = sorted(zip(capital, profits))
        n = len(projects)
        heap = []
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
                
            if len(heap) == 0:
                return w
            
            w -= heappop(heap)
        
        return w
            