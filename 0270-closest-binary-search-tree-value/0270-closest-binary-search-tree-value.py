# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        sorted_order = inorder(root)
        closet = float("inf")
        ans = 0
        for val in sorted_order:
            if abs(val-target) < closet:
                ans = val
                closet = abs(val-target)
        return ans
            
        