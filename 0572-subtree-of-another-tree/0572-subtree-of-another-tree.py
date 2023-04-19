# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        if not root:
            return
        
        if root.val == subRoot.val and self.check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def check(self, node, subNode):
        if not node and not subNode:
            return True
        
        if not node or not subNode:
            return False

        if node.val != subNode.val:
            return False

        left = self.check(node.left, subNode.left)
        right = self.check(node.right, subNode.right)

        return left and right
        
        
        
        