class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(curr_sum - target):
                    ans = curr_sum
                
                if curr_sum == target:
                    return target
                
                if curr_sum > target:
                    r -= 1
                else:
                    l += 1
        return ans