# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        
        def dfs(node, tree):
            if not node:
                return
            
            left = dfs(node.left, tree)
            right = dfs(node.right, tree)
            
            if not node.left and not node.right:
                tree.append(node.val)
                
            
            
        dfs(root1, tree1)
        dfs(root2, tree2)
        return tree1 == tree2
        
        