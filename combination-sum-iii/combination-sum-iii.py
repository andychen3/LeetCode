class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(num, curr_sum, index):
            if len(num) == k and curr_sum == n:
                ans.append(num[:])
                return
            
            for i in range(index, 10):
                if curr_sum + i <= n:
                    num.append(i)
                    backtrack(num, curr_sum + i, i + 1)
                    num.pop()
                
        
        ans = []
        backtrack([], 0, 1)
        return ans
        