# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.min_val = min(self.min_val, node.val-self.pre)
                self.pre = node.val
                dfs(node.right)
                
                
                
        self.min_val = float('inf')
        self.pre = float('-inf')
        dfs(root)
        return self.min_val

        