class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        
        for x, y in edges:
            graph[y] += 1
        
        print(graph)
        ans = []
        for i in range(n):
            if i not in graph:
                ans.append(i)
        return ans
        
#         def dfs(node):
#             for neighbor in graph[node]:
#                 if neighbor not in seen:
#                     seen.add(neighbor)
#                     dfs(neighbor)
                    
#         seen = set()
#         ans = []
#         for i in range(n):
#             if i not in seen:
#                 ans.append(i)
#                 seen.add(i)
#                 dfs(i)
#         return ans
        