class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            while nums[i] != i + 1:
                next_num = nums[i]-1
                if nums[i] == nums[next_num]:
                    break
                nums[i], nums[next_num] = nums[next_num], nums[i]
            i += 1
        
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans