class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr, i, total):
            if total == target:
                ans.append(arr[:])
                return
            
            
            for j in range(i, len(candidates)):
                nums = candidates[j]
                if nums + total <= target:
                    arr.append(nums)
                    backtrack(arr, j, total + nums)
                    arr.pop()
        ans = []
        backtrack([], 0, 0)
        return ans