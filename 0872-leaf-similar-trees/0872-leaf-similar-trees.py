# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr_1 = []
        arr_2 = []
        def dfs(node, arr):
            if not node:
                return 0
            
            if not node.left and not node.right:
                arr.append(node.val)
                
            return dfs(node.left, arr) + dfs(node.right, arr)
        
        dfs(root1, arr_1)
        dfs(root2, arr_2)
        return arr_1 == arr_2