class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        left = 0
        right = len(prefix) - 1
        
        while left < right:
            left_sum = prefix[left]
            right_sum = prefix[right] - left_sum
            
            if left_sum >= right_sum:
                valid_splits += 1
            
            left += 1
                
        return valid_splits
        