# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_max, curr_min):
            if not node:
                return 0
            
            self.ans = max(self.ans, curr_max-node.val, node.val-curr_min)
            
            dfs(node.left, max(curr_max, node.val), min(curr_min, node.val))
            dfs(node.right, max(curr_max, node.val), min(curr_min, node.val))
        
        self.ans = 0    
        dfs(root, root.val, root.val)
        return self.ans