class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        size = len(nums)
        
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            for j in range(index + 1, size):
                if j > index + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = size - 1
                while left < right:
                    total = num + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([num, nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return res