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
        
        if root.val == subRoot.val and self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
    def sameTree(self, root_node, sub_root):
        if not root_node and not sub_root:
            return True

        if not root_node or not sub_root:
            return False

        if root_node.val != sub_root.val:
            return False

        left = self.sameTree(root_node.left, sub_root.left)
        right = self.sameTree(root_node.right, sub_root.right)

        return left and right