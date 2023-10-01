class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            while nums[i] != i + 1:
                # To find the right index of the number it needs to exchange with
                curr = nums[i] - 1
                if nums[i] == nums[curr]:
                    break
                nums[i], nums[curr] = nums[curr], nums[i]
        
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans