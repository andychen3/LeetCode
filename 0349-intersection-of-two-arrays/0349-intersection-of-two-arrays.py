class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_set = set(nums1)
        num2_set = set(nums2)

        return list(num1_set & num2_set)
