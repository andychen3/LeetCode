from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counts = Counter(nums1)
        nums2_counts = Counter(nums2)

        ans = []
        for key, val in nums1_counts.items():
            if key in nums2_counts:
                ans += [key] * min(val, nums2_counts[key])
        
        return ans