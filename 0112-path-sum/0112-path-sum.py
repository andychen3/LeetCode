# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, curr=None) -> bool:
        if not root:
            return 
        
        if curr == None:
            curr = 0
        
        if not root.left and not root.right:
            return root.val+curr == targetSum

        
        return self.hasPathSum(root.left, targetSum, curr+root.val) or self.hasPathSum(root.right, targetSum, curr+root.val)

            
       