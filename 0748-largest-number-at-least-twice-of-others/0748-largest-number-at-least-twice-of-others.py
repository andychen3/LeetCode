class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_list = sorted(nums, reverse=True)

        if sorted_list[0] >= sorted_list[1]*2:
            return nums.index(sorted_list[0])
        return -1