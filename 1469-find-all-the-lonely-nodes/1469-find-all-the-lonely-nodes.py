# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode], arr=None) -> List[int]:
        if not root:
            return
        
        if arr == None:
            arr = []
        
        if not root.left or not root.right:
            if root.left:
                arr.append(root.left.val)
            if root.right:
                arr.append(root.right.val)
        
        self.getLonelyNodes(root.left, arr)
        self.getLonelyNodes(root.right, arr)
        
        return arr
            
        