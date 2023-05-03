class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        x = set(nums1)
        y = set(nums2)
        x_diff = x.difference(y)
        y_diff = y.difference(x)
        
        return [x_diff, y_diff]