# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        
        
        while queue:
            nodes_per_level = len(queue)
            res.append(queue[-1].val)
            
            for i in range(nodes_per_level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                    
        return res
            
        