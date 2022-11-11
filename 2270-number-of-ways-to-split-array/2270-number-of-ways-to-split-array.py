class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        count = 0
        
        for i in range(len(nums)-1):
            left += nums[i]
            if left >= right-left:
                count += 1
        return count