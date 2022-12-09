# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent):
            if not node:
                return 0
            

            if not node.left and not node.right:
                if parent.left == node:
                    return node.val

            left = dfs(node.left, node)
            right = dfs(node.right, node)
            
            
            return left+right
            
            
        
        return dfs(root, root)
        
        