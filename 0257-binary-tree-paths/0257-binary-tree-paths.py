# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node, tracker):
            if not node:
                return
            
            tracker.append(str(node.val))
            
            if not node.left and not node.right:
                ans.append("->".join(tracker))
            
            if node.left:
                left = dfs(node.left, tracker)
            
            if node.right:
                right = dfs(node.right, tracker)
            
            tracker.pop()

            
        dfs(root, [])
        return ans