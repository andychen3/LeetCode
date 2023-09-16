class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right_bound = sum(nums)
        left_total = 0

        for index, num in enumerate(nums):
            right_bound -= num
            if right_bound == left_total:
                return index
            left_total += num
        return -1