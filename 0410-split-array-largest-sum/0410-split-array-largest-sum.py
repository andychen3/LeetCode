class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(max_sum):
            curr_sum = 0
            splits = 0

            for num in nums:
                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    splits += 1
                    curr_sum = num
            # Splits have to add 1 because if in the instance the curr_sum doesn't exactly match
            # max_sum and that is the last element. You have to account for the last element which adds to
            # the split
            return splits+1 <= k
        
        # The left bound is not 1 because 
        # We need the max nums because if worse case we have to split the array and it has to be the total
        # max number to be able to split it that is the lowest possible number to be able to split
        # This example is portrayed when arr = [1,4,4] and k = 3. 1 Would not work because if it was 1 you
        # would be able to split the first element but then you can't split the other 2. So the min number
        # to allow the splitting to work is the maximum element of the array

        # We also used this template because we are looking for the min largest sum.
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left