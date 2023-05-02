class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr, curr_sum, i):
            if curr_sum == target:
                ans.append(arr[:])
                return
                
            for j in range(i, len(candidates)):
                num = candidates[j]
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if curr_sum + num > target:
                    return
                arr.append(num)
                backtrack(arr, curr_sum+num, j+1)
                arr.pop()
            
            
        candidates.sort()
        ans = []
        backtrack([], 0, 0)
        return ans