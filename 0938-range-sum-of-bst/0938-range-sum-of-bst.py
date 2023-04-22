# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        
        def dfs(node, low, high):
            if not node:
                return 0
            
            if low <= node.val <= high:
                self.sum += node.val
                
            if node.val > low:
                dfs(node.left, low, high)
            if node.val < high:
                dfs(node.right, low, high)
            
            
        dfs(root, low, high)
        return self.sum