class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        
        for x, y in edges:
            indegrees[y] += 1
            
        return [x for x, num in enumerate(indegrees) if num == 0]
        
        