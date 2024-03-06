class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        counts = 0
        
        for num in nums:
            if counts == 0:
                majority = num
            if num != majority:
                counts -= 1
            else:
                counts += 1
        return majority