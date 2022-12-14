# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node, path, targetSum):
            if not node:
                return 0
            
            path.append(node.val)
            targetSum -= node.val
            if targetSum == 0 and not node.left and not node.right:
                ans.append(path.copy())
                
            dfs(node.left, path, targetSum)
            dfs(node.right, path, targetSum)
            path.pop()
            
            
        dfs(root, [], targetSum)
        return ans
        