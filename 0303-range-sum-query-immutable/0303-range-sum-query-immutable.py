class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [nums[0]]
        
        for i in range(1, len(self.nums)):
            self.prefix.append(self.nums[i] + self.prefix[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left] + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)