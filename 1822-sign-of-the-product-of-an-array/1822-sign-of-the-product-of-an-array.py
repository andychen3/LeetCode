class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        
        for n in nums:
            total *= n
        
        if total > 0:
            return 1
        elif total < 0:
            return -1
        else:
            return 0