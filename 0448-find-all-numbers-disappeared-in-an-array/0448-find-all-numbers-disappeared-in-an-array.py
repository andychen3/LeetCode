class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            while nums[i] != i + 1:
                curr = nums[i]-1
                if nums[curr] == nums[i]:
                    break
                nums[i], nums[curr] = nums[curr], nums[i]
            i += 1
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
