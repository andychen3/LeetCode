class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # we get the right and left bounds
        right_sum = sum(nums) 
        left_total = 0

        for index, num in enumerate(nums):
            # We decrement the right bound first and check if it matches
            right_sum -= num
            # if match return index
            if right_sum == left_total:
                return index
            # then we increment the left bound
            left_total += num
        return -1