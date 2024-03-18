# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        list1 = inorder(root1)
        list2 = inorder(root2)
        
        ans = []
        
        left, right = 0, 0
        
        while left < len(list1) and right < len(list2):
            if list1[left] <= list2[right]:
                ans.append(list1[left])
                left += 1
            else:
                ans.append(list2[right])
                right += 1
        
        while left < len(list1):
            ans.append(list1[left])
            left += 1
        
        while right < len(list2):
            ans.append(list2[right])
            right += 1
        return ans