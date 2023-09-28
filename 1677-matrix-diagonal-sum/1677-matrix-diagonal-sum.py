class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        ans = 0
        
        for i in range(N):
            # Represents the diagonal
            ans += mat[i][i]
            # Represents the anti-diagonal from top right
            ans += mat[i][N-1-i]
        # IF square is odd you have to subtract out the middle
        if N % 2 != 0:
            ans -= mat[N//2][N//2]
        return ans

               