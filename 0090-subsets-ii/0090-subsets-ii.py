class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) > len(nums):
                return
            
            ans.append(curr[:])
            
            for j in range(i, len(nums)):
                num = nums[j]
                if j > i and nums[j] == nums[j-1]:
                    continue
                curr.append(num)
                backtrack(curr, j+1)
                curr.pop()
            
        nums.sort()  
        ans = []
        backtrack([], 0)
        return ans