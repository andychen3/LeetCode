class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {}
        curr = ans = 0
        
        for i, num in enumerate(nums):
            curr += num if num else -1
            if curr == 0:
                ans = max(ans, i + 1)
            elif curr in counts:
                ans = max(ans, i - counts[curr])
            else:
                counts[curr] = i
        return ans