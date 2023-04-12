class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for nums in nums1:
            ans.append(nums2.index(nums))
        return ans