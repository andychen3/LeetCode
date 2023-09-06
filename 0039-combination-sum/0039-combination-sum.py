class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, curr_sum, arr):
            if curr_sum == target:
                ans.append(arr[:])
                return
        
            for index in range(start, len(candidates)):
                if curr_sum + candidates[index] <= target:
                    arr.append(candidates[index])
                    backtrack(index, curr_sum + candidates[index], arr)
                    arr.pop()

        ans = []
        backtrack(0, 0, [])
        return ans