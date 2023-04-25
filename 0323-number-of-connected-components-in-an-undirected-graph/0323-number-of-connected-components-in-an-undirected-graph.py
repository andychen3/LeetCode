from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
            
        def dfs(node):
            for neighbors in graph[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    dfs(neighbors)
        
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans
                
            