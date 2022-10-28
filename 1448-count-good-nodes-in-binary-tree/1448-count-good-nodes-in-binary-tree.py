# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_node=None) -> int:
        if not root:
            return 0
        
        if max_node == None:
            max_node = float('-inf')
            
        max_node = max(max_node, root.val)
        left = self.goodNodes(root.left, max_node)
        right = self.goodNodes(root.right, max_node)
        good = left+right 
        
        if root.val >= max_node:
            good += 1 
        
        return good
        
        
        
        