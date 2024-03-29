from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            for x in num:
                counts[x] += 1
        
        ans = []
        for key, val in counts.items():
            if val == len(nums):
                ans.append(key)
        return sorted(ans)
