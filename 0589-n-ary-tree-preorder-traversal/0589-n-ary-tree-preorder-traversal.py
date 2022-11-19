"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        d = deque([root])
        res = []
        
        while d:
            node = d.popleft()
            res.append(node.val)
            
            for child in reversed(node.children):
                d.appendleft(child)
        return res
            
            
            
            
                
        