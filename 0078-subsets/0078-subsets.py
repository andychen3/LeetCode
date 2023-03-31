class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return
            
            ans.append(curr[:])
            
            for index in range(i, len(nums)):
                curr.append(nums[index])
                backtrack(curr, index + 1)
                curr.pop()
            
        ans = []
        backtrack([], 0)
        return ans