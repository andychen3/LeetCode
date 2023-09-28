class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        anti_diag = []
        diag = []

        N = len(mat)
        for row in range(N):
            for col in range(N):
                if row == N//2 and col == N//2:
                    anti_diag.append(mat[row][col])
                    continue
                if row + col == N - 1:
                    anti_diag.append(mat[row][col])
                if row - col == 0:
                    diag.append(mat[row][col])
        
        return sum(anti_diag) + sum(diag) 