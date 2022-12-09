# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, tree_list):
            if not node:
                return
            
            tree_list.append(str(node.val))
            nonlocal ans
            
            if not node.left and not node.right:
                ans += int("".join(tree_list), 2)
                
            left = dfs(node.left, tree_list)
            right = dfs(node.right, tree_list)
            tree_list.pop()
        
        dfs(root, [])
        return ans
        