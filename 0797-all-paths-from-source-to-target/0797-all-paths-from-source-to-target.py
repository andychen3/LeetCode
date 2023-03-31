class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, curr):
            if node == n-1:
                ans.append(curr[:])
                return
            
            for neighbors in graph[node]:
                curr.append(neighbors)
                backtrack(neighbors, curr)
                curr.pop()
            
        n = len(graph)
        ans = []
        backtrack(0, [0])
        return ans