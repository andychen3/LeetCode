class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Each row I switch the col and row and then after I do that I reverse the rows
        n = len(matrix)
        for r in range(n):
            # we need r + 1 because if not when it does the second iteration. 
            # It just reverses it back to normal
            for c in range(r + 1, n): 
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()
        return matrix