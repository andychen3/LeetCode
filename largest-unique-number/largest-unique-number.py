class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_int = -1
        
        for key, value in counter.items():
            if value == 1:
                max_int = max(max_int, key)            
        
        return max_int