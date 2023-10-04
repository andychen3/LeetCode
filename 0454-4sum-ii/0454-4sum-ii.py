from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        groups = defaultdict(int)

        for a in nums1:
            for b in nums2:
                groups[a+b] += 1
        ans = 0

        for c in nums3:
            for d in nums4:
                ans += groups[-(c+d)]
        return ans