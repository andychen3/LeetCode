class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i, num in enumerate(nums):
            left_sum += num

            if left_sum == right_sum:
                return i

            right_sum -= num
        
        return -1