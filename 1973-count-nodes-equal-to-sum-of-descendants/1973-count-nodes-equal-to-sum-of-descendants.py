# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.counts = 0
        def dfs(node):
            if not node:
                return 0
            total = dfs(node.left) + dfs(node.right)
            if total == node.val:
                self.counts += 1
            return total + node.val
            
        dfs(root)
        return self.counts