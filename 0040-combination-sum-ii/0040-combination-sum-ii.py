class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(arr, index, total):
            if total == target:
                ans.append(arr[:])
                return
        
            for i in range(index, len(candidates)):
                num = candidates[i]
                if i != index and candidates[i-1] == candidates[i]:
                    continue
                if total + num <= target:
                    arr.append(num)
                    backtrack(arr, i + 1, total + num)
                    arr.pop()
            
        
        ans = []
        backtrack([], 0, 0)
        return ans
        