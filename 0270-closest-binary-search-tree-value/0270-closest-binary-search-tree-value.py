# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if not node:
                return []
            
            return dfs(node.left) + [node.val] + dfs(node.right)
            
        values = dfs(root)
        print(values)
        ans = float('inf')
        for i in range(len(values)):
            if abs(values[i]-target) < abs(ans-target):
                ans = values[i]
        return ans
        