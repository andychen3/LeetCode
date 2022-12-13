# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        
        def dfs(node, paths):
            if not node:
                return
            nonlocal ans
            paths.append(chr(97+node.val))
            if not node.left and not node.right:
                if ans:
                    ans = min("".join(ans), "".join(reversed(paths)))
                else:
                    ans.append("".join(reversed(paths)))
            
            dfs(node.left, paths)
            dfs(node.right, paths)
            
            paths.pop()
        
        
        dfs(root, [])
        return "".join(ans)