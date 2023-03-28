# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, parent):
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        distance = 0 
        
        while queue and distance < k:
            queue_len = len(queue)
            
            for _ in range(queue_len):
                node = queue.popleft()
                
                for neighbors in [node.left, node.right, node.parent]:
                    if neighbors and neighbors not in seen:
                        seen.add(neighbors)
                        queue.append(neighbors)
            
            distance += 1
        
        return [node.val for node in queue]