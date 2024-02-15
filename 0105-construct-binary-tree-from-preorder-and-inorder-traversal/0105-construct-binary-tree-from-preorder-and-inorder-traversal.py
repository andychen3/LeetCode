# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            nonlocal preorder_idx
            if left > right:
                return None
            
            root = TreeNode(preorder[preorder_idx])
            
            preorder_idx += 1
            
            root.left = build(left, inorder_map[root.val] - 1)
            root.right = build(inorder_map[root.val]+1, right)
            return root
        
        preorder_idx = 0
        inorder_map = defaultdict(int)
        for idx, node in enumerate(inorder):
            inorder_map[node] = idx
        
        return build(0, len(preorder) - 1)