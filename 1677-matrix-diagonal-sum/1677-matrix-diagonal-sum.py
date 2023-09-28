class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = 0
        
        for i in range(N):
            ans += mat[i][i]

            ans += mat[i][N-1-i]
        if N % 2 != 0:
            ans -= mat[N//2][N//2]
        return ans

               