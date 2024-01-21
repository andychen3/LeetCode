class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        freq = 0
        
        for num in nums:
            if freq == 0:
                majority = num
                freq += 1
            elif num != majority:
                freq -= 1
            else:
                freq += 1
        return majority