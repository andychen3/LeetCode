class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # I know this is backtracking because of the input and the prompt
        # asking to find all possible paths
        def backtrack(node, path):
            if node == len(graph) - 1:
                ans.append(path[:])
            
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
        
        ans = []
        backtrack(0, [0])
        return ans