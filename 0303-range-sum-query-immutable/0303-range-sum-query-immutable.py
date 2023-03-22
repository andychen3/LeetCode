class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = self.createPrefix(self.nums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left] + self.nums[left]
        
        
    def createPrefix(self, nums):
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        return prefix
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)