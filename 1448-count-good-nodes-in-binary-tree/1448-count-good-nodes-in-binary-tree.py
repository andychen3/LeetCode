# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxNode):
            if not node:
                return 0
            
            ans = 0
            
            if node.val >= maxNode:
                ans += 1
            
            left = dfs(node.left, max(node.val, maxNode))
            right = dfs(node.right, max(node.val, maxNode))
            ans += left+right
            
            return ans
        
        return dfs(root, root.val)
        