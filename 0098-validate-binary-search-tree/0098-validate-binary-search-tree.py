# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, curr_min, curr_max):
            if not node:
                return True
            
            if not (curr_min < node.val < curr_max):
                return False
            
            left = dfs(node.left, curr_min, node.val)
            right = dfs(node.right, node.val, curr_max)
            return left and right
            
        return dfs(root, float("-inf"), float("inf"))