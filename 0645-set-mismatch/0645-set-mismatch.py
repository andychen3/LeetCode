from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        twice = None
        missing = None
        num_counter = Counter(nums)

        for num in range(1, len(nums) + 1):
            if num_counter[num] > 1:
                twice = num
            elif num not in num_counter:
                missing = num

        return [twice, missing]