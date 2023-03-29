# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if not node:
                return
            
            if node.val == target:
                self.closet = root.val
            
            if abs(target-node.val) < abs(target-self.closet):
                self.closet = node.val
            
            if node.val > target:
                dfs(node.left)
            
            if node.val < target:
                dfs(node.right)
            
            return
        
        self.closet = root.val
        dfs(root)
        
        return self.closet