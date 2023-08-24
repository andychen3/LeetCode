# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_node, max_node):
            if not node:
                return max_node - min_node

            left = dfs(node.left, min(min_node, node.val), max(max_node, node.val))
            right = dfs(node.right, min(min_node, node.val), max(max_node, node.val))

            return max(left, right)


        return dfs(root, root.val, root.val)