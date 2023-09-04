class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        # We start ans to 1 because we always have 1 element and since k can be 0
        # and an element minus itself will always be 0 so there will always be one
        # subsequence
        ans = 1 

        for right, num in enumerate(nums):
            # We do it this way so we don't need that second while loop and continue statement
            # we only increment answer when we start a new subsequence and set the next min val to the
            # start of the next subsequence
            if num - nums[left] > k:
                ans += 1    
                left = right 
        
        return ans

        