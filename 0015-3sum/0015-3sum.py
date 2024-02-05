class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for i, num in enumerate(nums):
            if num > 0:
                break
                
            if i > 0 and nums[i - 1] == num:
                continue
                
            left, right = i + 1, len(nums) - 1
            while left < right:
                triplet = num + nums[left] + nums[right]
                if triplet > 0:
                    right -= 1
                elif triplet < 0:
                    left += 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans