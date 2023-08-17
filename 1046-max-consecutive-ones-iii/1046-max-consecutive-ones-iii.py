class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length

