# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counts = 0
        def dfs(node, min_val):
            if not node:
                return 

            nonlocal counts
            if node.val >= min_val:
                counts += 1

            min_val = max(min_val, node.val)

            dfs(node.left, min_val) 
            dfs(node.right, min_val)
            
        dfs(root, root.val)
        return counts