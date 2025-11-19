from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = odds = 0
        counts = defaultdict(int)
        counts[0] = 1

        for num in nums:
            if num % 2 == 1:
                odds += 1
            ans += counts[odds - k]
            counts[odds] += 1
        
        return ans