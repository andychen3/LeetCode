# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 1)])
        ans = [float("-inf"), 0] # [sum, level]

        while queue:
            total = 0

            for _ in range(len(queue)):
                node, level = queue.popleft()
                total += node.val
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))
                
            if total > ans[0]:
                ans = [total, level]
        return ans[1]