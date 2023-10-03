class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        distinct = set()

        for num in nums:
            if num not in distinct:
                distinct.add(num)
            if len(distinct) == 3:
                return num
        return max(nums)
        