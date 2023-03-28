
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        
        def dfs(node):
            if node == destination:
                return True
            for neighbors in graph[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    if dfs(neighbors):
                        return True


        seen = {source}
        
        return dfs(source)