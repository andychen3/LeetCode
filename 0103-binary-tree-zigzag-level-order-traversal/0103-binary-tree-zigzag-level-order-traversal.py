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
        left_to_right = True

        while q:
            levels = deque()

            for _ in range(len(q)):
                node = q.popleft()
                # the root starts left to right
                # This is where you append the elements for the answer
                if left_to_right:
                    levels.append(node.val)
                else:
                    levels.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            left_to_right = not left_to_right
            
            ans.append(levels)
        return ans
                    
