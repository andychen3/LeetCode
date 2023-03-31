class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int: 
        def check(divisor):
            curr_sum = 0
            
            for n in nums:
                curr_sum += ceil(n/divisor)
            
            return curr_sum <= threshold
        
        
        left = 1
        right = sum(nums)
        total = sum(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
                