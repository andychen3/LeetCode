# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def postorder(node, arr):
            if not node:
                return []
            left = postorder(node.left, arr)
            right = postorder(node.right, arr)
            if not node.left and not node.right:
                arr.append(node.val)
            return arr
        
        return postorder(root1, []) == postorder(root2,[])