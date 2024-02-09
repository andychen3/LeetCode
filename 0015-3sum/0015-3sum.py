class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                triplets = num + nums[left] + nums[right]
                if triplets > 0:
                    right -= 1
                elif triplets < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return ans