class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        # Create a new matrix with dimensions switched
        transposed = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                # Switch row and column indices
                transposed[j][i] = matrix[i][j]
        
        return transposed
        