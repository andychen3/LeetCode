class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        def transpose():
            for r in range(N):
                for c in range(r+1, N):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                    
        transpose()
        for row in matrix:
            row.reverse()
        
        return matrix