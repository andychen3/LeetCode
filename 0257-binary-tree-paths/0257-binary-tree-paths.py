# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, paths):
            if not node:
                return 
            
            
            paths.append(str(node.val))
            
            if not node.left and not node.right:
                combined = "->".join(paths)
                ans.append(combined)
                
            dfs(node.left, paths)
            dfs(node.right, paths)
            
            paths.pop()
  
                
        dfs(root, [])
        return ans