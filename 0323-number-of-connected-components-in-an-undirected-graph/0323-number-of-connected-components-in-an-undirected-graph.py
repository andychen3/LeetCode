class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        def dfs(node, neighbors):
            seen.add(node)
            for x in neighbors:
                if x not in seen:
                    dfs(x, graph[x])
            
        seen = set()
        ans = 0
        for neigh in range(n):
            if neigh not in seen:
                dfs(neigh, graph[neigh])
                ans += 1

        return ans
            