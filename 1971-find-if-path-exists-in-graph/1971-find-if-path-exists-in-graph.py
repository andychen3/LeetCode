class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            if node == destination:
                return True
            
            seen.add(node)
            
            for neighbors in graph[node]:
                if neighbors not in seen:
                    found = dfs(neighbors)
                    if found:
                        return True
                    
            return False
        
        seen = set()
        return dfs(source)