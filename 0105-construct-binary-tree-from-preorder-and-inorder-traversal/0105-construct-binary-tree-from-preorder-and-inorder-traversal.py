# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            
            root = TreeNode(preorder[pre_idx])
            
            pre_idx += 1
            
            root.left = build(left, inorder_map[root.val] - 1)
            root.right = build(inorder_map[root.val] + 1, right)
            return root
        
        pre_idx = 0
        inorder_map = {}
        for idx, node in enumerate(inorder):
            inorder_map[node] = idx
        return build(0, len(preorder) - 1)