class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(arr):
            if len(arr) == n:
                string = [str(num) for num in arr]
                ans.append(int("".join(string)))
                return 
            
            for i in range(10):
                if i == 0 and len(arr) == 0:
                    continue
                    
                if len(arr) == 0 or abs(arr[-1] - i) == k:
                    arr.append(i)
                    backtrack(arr)
                    arr.pop()
        ans = []
        backtrack([])
        return ans