class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        freq_max = 0
        ans = left = 0
        
        for right, num in enumerate(nums):
            if num == max_elem:
                freq_max += 1
                
            while freq_max == k:
                if nums[left] == max_elem:
                    freq_max -= 1
                left += 1
            ans += left
        return ans
        