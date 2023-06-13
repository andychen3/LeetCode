class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        N = len(nums)
        
        for index, num in enumerate(nums):
            left = index + 1
            right = N - 1
            while left < right:
                _sum = num + nums[left] + nums[right]
                if _sum < target:
                    ans += right - left
                    left += 1
                else:
                    right -= 1
        return ans
        