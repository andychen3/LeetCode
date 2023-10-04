# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_map = defaultdict(int)
        res = []
        def dfs(node):
            if not node:
                return ""
            
            rep = f"{dfs(node.left)}{node.val}{dfs(node.right)}#"
            hash_map[rep] += 1
            if hash_map[rep] == 2:
                res.append(node)
            return rep
        dfs(root)
        return res