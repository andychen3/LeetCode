from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        max_num = -1
        
        for key, val in counter.items():
            if val == 1:
                max_num = max(max_num, key)
                
        return max_num