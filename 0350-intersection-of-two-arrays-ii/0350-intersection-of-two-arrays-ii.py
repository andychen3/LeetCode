from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = Counter(nums1)
        res = []

        for num in nums2:
            if num in nums1_counts and nums1_counts[num] > 0:
                res.append(num)
                nums1_counts[num] -= 1
        return res
