# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, curr_max):
            if not node:
                return
            
            if node.val >= curr_max:
                self.ans += 1
            curr_max = max(curr_max, node.val)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        
        dfs(root, root.val)
        return self.ans