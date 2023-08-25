# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(node, closest):
            if not node:
                return closest
            
            closest = min(node.val, closest, key=lambda x: (abs(target-x), x))

            if target < node.val:
                return dfs(node.left, closest)
            else:
                return dfs(node.right, closest)



        return dfs(root, root.val)
