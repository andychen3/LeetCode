from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(node):
            if node in seen:
                return False
            if graph[node] == []:
                return True
            seen.add(node)
            
            for neighbors in graph[node]:
                if not dfs(neighbors):
                    return False
            seen.remove(node)
            graph[node] = []
            return True
            
        
        seen = set()
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True