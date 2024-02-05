"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}
        
        def dfs(root):
            if root in graph:
                return graph[root]
            
            new_node = Node(root.val)
            graph[root] = new_node
            for neighbors in root.neighbors:
                new_node.neighbors.append(dfs(neighbors))
            return new_node
            
            
        
        return dfs(node) if node else None
        
        