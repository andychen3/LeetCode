# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dups = defaultdict(int)
        ans = []
        def dfs(node):
            if not node:
                return ""
            
            serialize = f"{dfs(node.left)}{node.val}{dfs(node.right)}#"
            dups[serialize] += 1
            if dups[serialize] == 2:
                ans.append(node)
            return serialize
        dfs(root)
        return ans