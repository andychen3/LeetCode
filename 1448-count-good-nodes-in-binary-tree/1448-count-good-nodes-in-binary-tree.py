# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_node=None, good=None) -> int:
        if not root:
            return 0
        
        if max_node == None:
            max_node = float('-inf')
            good = 0
            
        if root.val >= max_node:
            max_node = max(max_node, root.val)
            good += 1
            
        return (root.val >= max_node)+self.goodNodes(root.left, max_node, good) + self.goodNodes(root.right, max_node, good)
        
        
        
        