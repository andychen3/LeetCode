class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                # check top left
                if 0 <= r-1 and 0 <= c-1: 
                    if matrix[r-1][c-1] != matrix[r][c]:
                        return False
                if r+1 < row and c+1 < col: 
                    if matrix[r+1][c+1] != matrix[r][c]:
                        return False
        return True
        