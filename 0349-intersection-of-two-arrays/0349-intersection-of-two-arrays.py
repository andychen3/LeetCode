class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for nums in nums1:
            if nums in nums2 and nums not in res:
                res.append(nums)
        return res
        