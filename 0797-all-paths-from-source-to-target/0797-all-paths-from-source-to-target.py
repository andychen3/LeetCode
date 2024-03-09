class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        def backtrack(arr, i):
            if i == n:
                ans.append(arr[:])
                return
            
            for node in graph[i]:
                arr.append(node)
                backtrack(arr, node)
                arr.pop()
        ans = []
        backtrack([0], 0)
        return ans
                