
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counts = {}
        ans = 0
        
        for a in nums1:
            for b in nums2:
                counts[a+b] = counts.get(a+b, 0) + 1
        
        
        for c in nums3:
            for d in nums4:
                if -(c+d) in counts:
                    ans += counts[-(c+d)]
        return ans