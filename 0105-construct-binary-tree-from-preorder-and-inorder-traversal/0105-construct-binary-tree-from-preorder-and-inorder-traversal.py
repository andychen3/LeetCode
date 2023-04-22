# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(left, right):
            nonlocal preorder_idx
            if left > right:
                return
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            mid = hash_map[root.val]
            root.left = dfs(left, mid -1)
            root.right = dfs(mid + 1, right)
            return root
        
        preorder_idx = 0
        hash_map = {node: index for index, node in enumerate(inorder)}
        return dfs(0, len(inorder)-1)