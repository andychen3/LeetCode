from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED = 0
        BLUE = 1
        
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
            
        for x,y in blueEdges:
            graph[BLUE][x].append(y)
            
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0,RED), (0,BLUE)}
        ans = [float("inf")]*n
        
        while queue:
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)
            
            for neighbors in graph[color][node]:
                if (neighbors, 1 - color) not in seen:
                    seen.add((neighbors, 1 - color))
                    queue.append((neighbors, 1 - color, steps + 1))
        
        return [num if num != float("inf") else -1 for num in ans]