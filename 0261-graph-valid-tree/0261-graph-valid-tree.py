from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            if node in seen:
                return False
            seen.add(node)
            
            for neighbor in graph[node]:
                dfs(neighbor)
                    
        seen = set()
        
        dfs(0)
        return len(seen) == n
