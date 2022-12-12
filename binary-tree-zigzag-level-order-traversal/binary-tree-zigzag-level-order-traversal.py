# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = collections.deque([root])
        direction = 'left'
        
        while q:
            levels = len(q)
            curr_level = []
            
            for _ in range(levels):
                if direction == 'left':
                    node = q.popleft()
                else:
                    node = q.pop()
                curr_level.append(node.val)
                
                if direction is 'left':
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                else:
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                            
            ans.append(curr_level)
            
            if direction == 'left':
                direction = 'right'
            else:
                direction = 'left'
        
        return ans
                
        