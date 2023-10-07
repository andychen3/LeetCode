from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums2)
        ans = []

        for num in nums1:
            if num in counts and counts[num] > 0:
                ans.append(num)
                counts[num] -= 1

        return ans