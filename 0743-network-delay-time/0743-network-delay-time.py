import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, z in times:
            graph[x - 1].append([y - 1, z])
            
        distances = [inf] * n
        distances[k-1] = 0
        min_heap = [(0, k - 1)]
        
        while min_heap:
            curr_dist, node = heappop(min_heap)
            if curr_dist > distances[node]:
                continue
            
            for nei, weight in graph[node]:
                distance = curr_dist + weight
                if distance < distances[nei]:
                    distances[nei] = distance
                    heappush(min_heap, (distance, nei))
        ans = max(distances)
        return ans if ans != inf else -1
        