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
        
        queue = deque([root])
        ans = []
        
        while queue:
            queue_len = len(queue)
            curr_sum = 0
            
            for _ in range(queue_len):
                node = queue.popleft()
                curr_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
            ans.append(curr_sum)
        
        return ans[-1]