from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_map = defaultdict(int)

        for i1 in nums1:
            for i2 in nums2:
                hash_map[i1+i2] += 1
        
        ans = 0
        for i3 in nums3:
            for i4 in nums4:
                ans += hash_map[-(i3+i4)]
        return ans
        