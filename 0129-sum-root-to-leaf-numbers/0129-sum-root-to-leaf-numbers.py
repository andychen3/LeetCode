# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(node, tree_list):
            if not node:
                return 
            
            tree_list.append(str(node.val))
            
            if not node.left and not node.right:
                res[0] += int("".join(tree_list))
                
            
            left = dfs(node.left, tree_list)
            right = dfs(node.right, tree_list)
            tree_list.pop()
            
            
                
        
        dfs(root, [])
        return res[0]
        