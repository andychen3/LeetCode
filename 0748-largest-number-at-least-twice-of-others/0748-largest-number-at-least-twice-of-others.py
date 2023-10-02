class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)

        if sorted_num[-2]*2 <= sorted_num[-1]:
            return nums.index(sorted_num[-1])
        return -1

