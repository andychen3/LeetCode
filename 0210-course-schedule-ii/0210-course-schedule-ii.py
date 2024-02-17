from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
            
            
        def dfs(node):
            if node in seen:
                return False
            if node in visited:
                return True
            
            seen.add(node)
            for neighbors in graph[node]:
                if not dfs(neighbors):
                    return False
            
            seen.remove(node)
            visited.add(node)
            ans.append(node)
            return True
            
        seen = set()
        visited = set()
        ans = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
            
            