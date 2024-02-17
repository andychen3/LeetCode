from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
            
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        visited = []
        
        while queue:
            node = queue.popleft()
            visited.append(node)
            
            for neighbors in graph[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        
        if len(visited) == numCourses:
            return visited
        return []