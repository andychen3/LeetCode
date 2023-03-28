# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_val, min_val):
            if not node:
                return
            
            nonlocal max_num
            
            max_num = max(abs(node.val-max_val), max_num, abs(node.val-min_val))
            left = dfs(node.left, max(node.val, max_val), min(node.val, min_val))
            right = dfs(node.right, max(node.val, max_val), min(node.val, min_val))
            
            return
             
        max_num = 0
        dfs(root, root.val, root.val)
        return max_num
        