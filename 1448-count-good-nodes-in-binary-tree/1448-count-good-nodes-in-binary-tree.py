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
                return 
            
            if node.val >= maxNode:
                self.good += 1
            
            dfs(node.left, max(node.val, maxNode))
            dfs(node.right, max(node.val, maxNode))
        
        self.good = 0
        dfs(root, root.val)
        return self.good
        