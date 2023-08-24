# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # What is true about the properties of a bst?
        # All values to the left of root are less than it
        # All values to the right of root are greater
        # Takes log(n) to find a value because values are in sorted order and you will perform Binary search
        # Inorder traversal will return a sorted order list of the tree

        # If an empty tree the value you want to insert becomes the root
        if not root:
            return TreeNode(val)

        # check if the current value is either less than or greater than root
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val >= root.val:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
        

        