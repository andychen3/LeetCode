# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node, closet):
            if not node:
                return closet
            
            closet = min(node.val, closet, key=lambda x: (abs(target-x),x))
            if node.val > target:
                return dfs(node.left, closet)
            else:
                return dfs(node.right, closet)
        return dfs(root, root.val)