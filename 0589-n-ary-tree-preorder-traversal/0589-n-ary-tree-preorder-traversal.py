"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if not node:
                return
            ans.append(node.val)
            
            for val in node.children:
                dfs(val)
                
            
            
            
        dfs(root)
        return ans