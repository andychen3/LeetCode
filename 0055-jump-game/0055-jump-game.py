class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = nums[0]
        
        for i in range(1, len(nums)):
            if start <= 0:
                return False
            start -= 1
            start = max(nums[i], start)
        return True