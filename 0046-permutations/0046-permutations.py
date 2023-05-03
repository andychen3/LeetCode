class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()
                
            
            
        ans = []
        backtrack([])
        return ans