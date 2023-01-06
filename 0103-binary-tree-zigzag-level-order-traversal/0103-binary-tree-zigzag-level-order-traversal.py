# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        flag = True
        
        while queue:
            q_len = len(queue)
            curr_level = deque()
            
            for _ in range(q_len):
                node = queue.popleft()
                if flag:
                    curr_level.append(node.val)    
                else:
                    curr_level.appendleft(node.val)    
                        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if flag:
                flag = False
            else:
                flag = True
            ans.append(curr_level)
        return ans
                
                
            
        