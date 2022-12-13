# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_val = float('inf')
        prev = float('-inf')
        def dfs(node):
            nonlocal min_val, prev
            # nonlocal prev
            if node:
                dfs(node.left)
                min_val = min(min_val, node.val-prev)
                prev = node.val
                dfs(node.right)
        
        dfs(root)
        return min_val