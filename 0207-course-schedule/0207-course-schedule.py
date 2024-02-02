from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return visited == numCourses
            
            
