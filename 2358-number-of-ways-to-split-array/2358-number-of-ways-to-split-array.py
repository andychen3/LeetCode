class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        ans = 0
        n = len(nums) - 1

        for j in range(len(nums) - 1):
            remaining_total = prefix[n] - prefix[j]
            if prefix[j] >= remaining_total:
                ans += 1
        
        return ans