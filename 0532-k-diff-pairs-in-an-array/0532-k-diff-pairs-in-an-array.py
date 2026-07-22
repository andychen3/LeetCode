
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        unique_set = set()

        for i, num in enumerate(nums):
            for second_num in range(i + 1, n):
                if abs(num - nums[second_num]) == k and (num, nums[second_num]) not in unique_set:
                    pair = (min(num, nums[second_num]), max(num, nums[second_num]))
                    unique_set.add(pair)

        return len(unique_set)