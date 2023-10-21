# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        arr = inorder(root)
        min_dist = float("inf")
        ans = 0
        for num in arr:
            if abs(target - num) < min_dist:
                min_dist = abs(target - num)
                ans = num
        return ans