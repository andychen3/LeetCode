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
        ans = 0

        while d:
            ans = 0

            for _ in range(len(d)):
                node = d.popleft()
                ans += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            
        
        return ans
