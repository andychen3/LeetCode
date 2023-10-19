# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, max_node, min_node):
            if not node:
                return 
            
            dfs(node.left, max(node.val, max_node), min(min_node, node.val))
            dfs(node.right, max(node.val, max_node), min(min_node, node.val))
            self.diff = max(abs(max_node - node.val), self.diff, abs(min_node - node.val))
            return
        
        self.diff = 0    
        dfs(root, root.val, root.val)
        return self.diff