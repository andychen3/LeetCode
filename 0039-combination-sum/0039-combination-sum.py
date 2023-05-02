class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, curr_sum, j):
            if curr_sum == target:
                ans.append(curr[:])
                return
            
            
            for i in range(j, len(candidates)):
                num = candidates[i]
                if curr_sum + num <= target:
                    curr.append(num)

                    backtrack(curr, curr_sum + num, i)
                    curr.pop()
        
        ans = []
        backtrack([], 0, 0)
        return ans