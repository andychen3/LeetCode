# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        ans = []
        mapping = defaultdict(list)
        
        while queue:
            for _ in range(len(queue)):
                node, offset = queue.popleft()
                mapping[offset].append(node.val)
                if node.left:
                    queue.append([node.left, offset - 1])
                if node.right:
                    queue.append([node.right, offset + 1])
        
        ans = []
        for key in sorted(mapping.keys()):
            ans.append(mapping[key])
        return ans
        