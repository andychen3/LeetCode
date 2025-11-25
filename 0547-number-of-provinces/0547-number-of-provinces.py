from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r, c = len(isConnected), len(isConnected[0])
        graph = defaultdict(list)

        for row in range(r):
            for col in range(c):
                if isConnected[row][col] == 1:
                    graph[row].append(col)
        
        def dfs(node):
            seen.add(node)

            for element in graph[node]:
                if element not in seen:
                    dfs(element)

        res = 0
        seen = set()

        for node in graph:
            if node not in seen:
                res += 1
                dfs(node)
        
        return res
        