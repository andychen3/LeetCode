class Solution:
    def rob(self, nums: List[int]) -> int:
        # To avoid out of bounds error from setting base case
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)

        # Base cases
        back_two = nums[0]
        back_one = max(nums[0], nums[1])
        
        for i in range(2, n):
            # back_two becomes back_one, and back_one gets updated
            # We save back_one to temp because we want this value to be the new back_two value
            # We perform the recurrence relation on back_one because back_one is the value that is movign 
            # forward. 
            # That is why we return back_one because at the end of the for loop it holds the answer at the 
            # last index.
            temp = back_one
            back_one = max(back_one, back_two + nums[i])
            back_two = temp

            # back_one, back_two = max(back_one, back_two + nums[i]), back_one

        return back_one