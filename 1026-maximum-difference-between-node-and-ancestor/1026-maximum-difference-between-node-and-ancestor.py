# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        def dfs(node, min_val, max_val):
            if not node:
                self.max_val = max(self.max_val, abs(min_val-max_val))
                return 0
            
            left = dfs(node.left, min(node.val, min_val), max(max_val, node.val))
            right = dfs(node.right, min(node.val, min_val), max(max_val, node.val))
            
            
            
            
            
        dfs(root, root.val, root.val)
        return self.max_val