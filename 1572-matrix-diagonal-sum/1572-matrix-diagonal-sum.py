class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        row = len(mat)
        col = len(mat[0])
        
        for r in range(row):
            for c in range(col):
                if (r-c) == 0:
                    _sum += mat[r][c]
                elif (r+c) == col-1:
                    _sum += mat[r][c]
        return _sum
        