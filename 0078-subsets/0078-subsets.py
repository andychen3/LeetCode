class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr, start):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 
            ans.append(arr[:])
        
            for i in range(start, len(nums)):
                num = nums[i]
                if num not in arr:
                    arr.append(num)
                    backtrack(arr, i + 1)
                    arr.pop()
        
        
        ans = []
        backtrack([], 0)
        return ans