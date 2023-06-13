class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                    continue
            for j in range(index+1, len(nums)-2):
                if j > index+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    _sum = num + nums[j] + nums[left] + nums[right]
                    if _sum == target:
                        ans.append([num, nums[j], nums[left], nums[right]])
                        # ans.add((num, nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif _sum > target:
                        right -= 1
                    else:
                        left += 1
        return ans