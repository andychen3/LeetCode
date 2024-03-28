from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        
        
        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for neighbors in graph[node]:
                dfs(neighbors)
        
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        seen = set()
        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans