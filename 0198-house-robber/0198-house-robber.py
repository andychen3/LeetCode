class Solution:
    def rob(self, nums: List[int]) -> int:
        # Check if only one element then return that one house
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        # We only multiply n instead of n + 1 because the first index you always rob
        # if one house.
        # it's different from fibonacci because the 0th index you have to have it as 0.
        # while here it is not. You can rewrite it to have 0 as the index if you want.
        arr = [0] * n
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])

        for i in range(2, n):
            arr[i] = max(arr[i - 2] + nums[i], arr[i-1])
        
        return arr[n-1]
