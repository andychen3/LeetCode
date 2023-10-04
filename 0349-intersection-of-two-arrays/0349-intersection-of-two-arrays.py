class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set = set(nums1)
        ans = []
        
        for num in set(nums2):
            if num in num_set:
                ans.append(num)
        return ans
