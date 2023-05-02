class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            
            for n in nums:
                if n not in arr:
                    arr.append(n)    
                    backtrack(arr)
                    arr.pop()

            
            
        ans = []
        backtrack([])
        return ans
    
    