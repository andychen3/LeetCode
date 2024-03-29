from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        
        for x, y in connections:
            roads.add((x, y))
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            ans = 0
            for neighbors in graph[node]:
                if neighbors not in seen:
                    if (node, neighbors) in roads:
                        ans += 1
                    
                    seen.add(neighbors)
                    ans += dfs(neighbors)
            return ans
        
        seen = {0}
        return dfs(0)