class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(isConnected)

        def dfs(node):
            for neighbors in graph[node]:
                if neighbors not in seen:
                    seen.add(neighbors)
                    dfs(neighbors)
        
        
        for x in range(n):
            for y in range(x + 1, n):
                if isConnected[x][y]:
                    graph[x].append(y)
                    graph[y].append(x)
        
        
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                ans += 1
        return ans
        
        