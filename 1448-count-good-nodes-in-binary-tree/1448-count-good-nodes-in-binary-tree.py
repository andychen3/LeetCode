# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, max_val):
            if not node:
                return
            
            if node.val >= max_val:
                self.ans += 1
            left = dfs(node.left, max(node.val, max_val))
            right = dfs(node.right, max(node.val, max_val))
            
        
        dfs(root, root.val)
        return self.ans