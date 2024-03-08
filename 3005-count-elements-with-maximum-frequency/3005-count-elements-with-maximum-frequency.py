from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = max(counts.values())
        ans = 0
        
        for key, val in counts.items():
            if val == max_freq:
                ans += val
        return ans
            