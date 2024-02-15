class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, num):
        rob1, rob2 = 0,0
        
        for house in num:
            maxRob = max(rob2, house + rob1)
            rob1 = rob2
            rob2 = maxRob
        return rob2