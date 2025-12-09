class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []

        for i, num in enumerate(nums):
            smaller = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] < num:
                    smaller += 1
            res.append(smaller)
        return res