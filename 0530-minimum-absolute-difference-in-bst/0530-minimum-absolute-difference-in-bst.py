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
            
            left = inorder(node.left)
            right = inorder(node.right)
            
            return left + [node.val] + right
        
        sorted_list = inorder(root)
        n = len(sorted_list)
        ans = float("inf")
        
        for i in range(n-1):
            ans = min(ans, sorted_list[i+1] - sorted_list[i])
        return ans