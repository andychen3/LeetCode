class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse=True)
        nums2.sort()
        res = 0
        
        for i, val in enumerate(nums1):
            res += val*nums2[i]
        return res
        