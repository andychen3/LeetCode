# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, Sum):
            if not node:
                return False
            
            Sum += node.val
            
            if not node.left and not node.right and Sum == targetSum:
                return True
            
            left = dfs(node.left, Sum)
            right = dfs(node.right, Sum)
            return left or right
        
        
        Sum = 0
        return dfs(root, Sum)
        
#         if not root:
#             return False
        
#         if not root.left and not root.right and targetSum-root.val == 0:
#             return True
        
#         left = self.hasPathSum(root.left, targetSum-root.val)
#         right = self.hasPathSum(root.right, targetSum-root.val)
        
#         return left or right
        