# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = deque([root])
        ans = []

        while d:
            curr_sum = 0

            for _ in range(len(d)):
                node = d.popleft()
                curr_sum += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(curr_sum)
        
        return ans[-1]
