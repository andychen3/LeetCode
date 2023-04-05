class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        def transpose(r, c):
            for rows in range(N):
                for cols in range(rows+1, N):
                    matrix[rows][cols], matrix[cols][rows] = matrix[cols][rows], matrix[rows][cols]
            
        
        transpose(N,N)
        
        for r in range(N):
            matrix[r].reverse()
            
        return matrix