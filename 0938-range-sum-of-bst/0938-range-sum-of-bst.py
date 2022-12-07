# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            
            nonlocal Sum
            
            if node.val >= low and node.val <= high:
                Sum += node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return Sum
        
        Sum =  0
        return dfs(root)