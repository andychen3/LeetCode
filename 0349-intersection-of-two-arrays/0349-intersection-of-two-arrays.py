class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        return nums1_set&nums2_set
        
        
#         res = []
        
#         for nums in nums1:
#             if nums in nums2 and nums not in res:
#                 res.append(nums)
#         return res
        