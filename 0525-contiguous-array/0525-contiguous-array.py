from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        zero = 0
        ones = 0

        for i, num in enumerate(nums):
            if num == 1:
                ones += 1
            else:
                zero += 1

            curr = zero - ones

            if curr == 0:
                ans = zero + ones
            elif curr not in counts:
                counts[curr] = i
            else:
                ans = max(ans, i - counts[curr])
        
        return ans