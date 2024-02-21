class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = [node for node in range(n)]
        rank = [1] * n
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
            
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False
            
            if rank[root1] < rank[root2]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
            
            return True
            
        
        for x, y in edges:
            if not union(x, y):
                return False
            
        return True
            
            
            
        
        