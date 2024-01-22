from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_val = max(counts.values())
        
        for key, val in counts.items():
            if val == max_val:
                return key
            