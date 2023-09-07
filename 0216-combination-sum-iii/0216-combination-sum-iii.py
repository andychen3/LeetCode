class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(arr, curr, i):
            if len(arr) == k and curr == n:
                ans.append(arr[:])
                return
            
            for j in range(i, 10):
                # This is to make sure that when i add the sum to the next number it's still
                # within n else i skip it.
                if curr + j <= n:
                    arr.append(j)
                    # I do j + 1 because they say that all numbers must be used at most once
                    # By doing this i skip the previous number
                    backtrack(arr, curr + j, j + 1)
                    arr.pop()

        ans = []
        backtrack([], 0, 1)
        return ans