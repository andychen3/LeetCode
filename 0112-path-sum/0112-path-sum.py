# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, total):
            if not node:
                return 0
            
            total += node.val
            if not (node.left or node.right) and total == targetSum:
                return True
            left = dfs(node.left, total)
            right = dfs(node.right, total)
            
            return left or right
        
        total = 0
        return dfs(root, total)

        
#         if not root:
#             return 0
        
#         targetSum -= root.val
#         if not root.left and not root.right:
#             return targetSum == 0
        
#         left = self.hasPathSum(root.left, targetSum)
#         right = self.hasPathSum(root.right, targetSum)
        
#         return left or right
        