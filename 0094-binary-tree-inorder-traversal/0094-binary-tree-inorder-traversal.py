# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [root]
        res = []
        
        while stack:
            while root and root.left:
                stack.append(root.left)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            root = node.right
        return res
            
                
            
            
            
            

            
        