class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(arr, i, total):
            if total == target:
                ans.append(arr[:])
                return
            
            for j in range(i, len(candidates)):
                if i != j and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j] + total <= target:
                    arr.append(candidates[j])
                    backtrack(arr, j+1, total + candidates[j])
                    arr.pop()
                    
        ans = []
        backtrack([],0,0)
        return ans