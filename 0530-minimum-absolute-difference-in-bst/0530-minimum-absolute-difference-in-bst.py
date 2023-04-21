# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        res = inorder(root)
        min_diff = float('inf')
        
        for i in range(1, len(res)):
            min_diff = min(abs(res[i] - res[i-1]), min_diff)
        return min_diff