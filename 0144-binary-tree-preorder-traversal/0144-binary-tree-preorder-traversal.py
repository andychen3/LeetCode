# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.list = []
        def dfs(node):
            if not node:
                return 
            
            self.list.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right)
            return 

        dfs(root)
        return self.list