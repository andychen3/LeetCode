# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = 0

        def dfs(node, lowest, highest):
            if not node:
                return

            lowest = min(lowest, node.val)
            highest = max(highest, node.val)

            self.diff = max(abs(lowest - highest), self.diff)

            dfs(node.left, lowest, highest)
            dfs(node.right, lowest, highest)
        
        dfs(root, root.val, root.val)
        return self.diff