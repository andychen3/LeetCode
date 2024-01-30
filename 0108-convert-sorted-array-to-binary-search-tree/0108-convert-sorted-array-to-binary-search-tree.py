# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            
            node = TreeNode(nums[mid])
            node.left = create_tree(left, mid - 1)
            node.right = create_tree(mid + 1, right)
            return node
            
        return create_tree(0, len(nums) - 1)