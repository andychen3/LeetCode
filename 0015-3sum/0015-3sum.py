class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        
        for index, num in enumerate(nums):
            # if index > 0 and num == nums[index-1]:
            #     continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                _sum = num + nums[left] + nums[right]
                if _sum == 0:
                    ans.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    left += 1
        return ans