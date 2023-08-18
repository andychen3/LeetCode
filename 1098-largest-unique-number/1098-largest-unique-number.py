from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_counts = Counter(nums)
        unique_number = [num for num, count in num_counts.items() if count == 1]
        
        return max(unique_number, default=-1)
            
        