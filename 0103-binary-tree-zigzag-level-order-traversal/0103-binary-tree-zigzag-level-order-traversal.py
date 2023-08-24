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
        
        q = deque([root])
        ans = []
        left_to_right = False

        while q:
            levels = deque()

            for _ in range(len(q)):
                node = q.popleft()
                if left_to_right:
                    levels.appendleft(node.val)
                else:
                    levels.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if left_to_right:
                left_to_right = False
            else:
                left_to_right = True
            
            ans.append(levels)
        return ans
                    
