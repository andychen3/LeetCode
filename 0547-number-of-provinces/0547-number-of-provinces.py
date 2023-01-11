class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        seen = set()
        ans = 0
        graph = collections.defaultdict(list)
        
        for r in range(N):
            for c in range(r+1, N):
                if isConnected[r][c] == 1:
                    graph[r].append(c)
                    graph[c].append(r)

        def dfs(node):
            for neighbors in graph[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    dfs(neighbors)
        
        for i in range(N):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans
        
            
        
    
        