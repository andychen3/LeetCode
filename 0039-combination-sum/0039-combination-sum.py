class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(arr, total, index):
            if total == target:
                ans.append(arr[:])
                return
        
            for i in range(index, len(candidates)):
                num = candidates[i]
                if total + num <= target:
                    arr.append(num)
                    backtrack(arr, total + num, i)
                    arr.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans