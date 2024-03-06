class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        counts = 0
        
        for num in nums:
            if majority != num and counts == 0:
                majority = num
                counts = 0
            elif num != majority:
                counts -= 1
            else:
                counts += 1
        return majority