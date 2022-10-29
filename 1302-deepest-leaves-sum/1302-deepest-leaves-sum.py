# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
        
        queue = collections.deque([root])
        res = 0
        
        while queue:
            levels = len(queue)
            res = 0
            
            for _ in range(levels):
                node = queue.popleft()
                res += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        