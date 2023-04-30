from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            seen.add(node)
            for neighbors in graph[node]:
                if neighbors not in seen:
                    dfs(neighbors)
        
        seen = set()
        dfs(0)
        
        return len(seen) == n
            
            