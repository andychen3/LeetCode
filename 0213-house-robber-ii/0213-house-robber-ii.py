class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_house(nums[1:]), self.rob_house(nums[:-1]))
        
    def rob_house(self, arr):
        rob1, rob2 = 0, 0

        for cash in arr:
            rob1, rob2 = max(rob1, rob2 + cash), rob1
        return rob1
