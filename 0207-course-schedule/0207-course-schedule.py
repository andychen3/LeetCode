from collections import deque, defaultdict
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
            
            for neighbors in graph[node]:
                indegree[neighbors] -= 1
                if indegree[neighbors] == 0:
                    queue.append(neighbors)
        return visited == numCourses
