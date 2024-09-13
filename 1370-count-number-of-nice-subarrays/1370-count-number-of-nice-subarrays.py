from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        total = ans = 0

        for num in nums:
            total += num % 2
            ans += counts[total - k]
            counts[total] += 1
        return ans