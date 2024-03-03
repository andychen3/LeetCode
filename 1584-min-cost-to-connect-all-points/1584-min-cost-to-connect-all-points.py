import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        graph = {i:[] for i in range(n)}
        
        for i in range(n):
            x, y = points[i]
            for j in range(i + 1, n):
                x1, y1 = points[j]
                dist = abs(x - x1) + abs(y - y1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        res = 0
        min_heap = [[0,0]]
        seen = set()
        
        while len(seen) < n:
            cost, node = heappop(min_heap)
            if node in seen:
                continue
            res += cost
            seen.add(node)
            
            for dist, nei in graph[node]:
                if nei not in seen:
                    heappush(min_heap, [dist, nei])
        return res