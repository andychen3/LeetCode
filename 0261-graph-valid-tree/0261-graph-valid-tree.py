class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return False
    
        self.parent[root1] = root2
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        unionFind = UnionFind(n)
        
        for x, y in edges:
            if not unionFind.union(x, y):
                return False
        return True