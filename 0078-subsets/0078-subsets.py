class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, arr):
            if i == n:
                ans.append(arr[:])
                return
            
            ans.append(arr[:])
        
            for j in range(i, n):
                arr.append(nums[j])
                backtrack(j + 1, arr)
                arr.pop()

        n = len(nums)
        ans = []
        backtrack(0, [])
        return ans
        