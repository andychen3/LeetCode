from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            for neighbors in graph[node]:
                if neighbors not in seen and neighbors not in res:
                    seen.add(neighbors)
                    dfs(neighbors)
        
        seen = {0}
        res = set(restricted)
        dfs(0)
        
        return len(seen)