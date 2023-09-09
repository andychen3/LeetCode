class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # We can do either way to start from zero or start from 1. If we start from 0
        # we have to subtract 1 from rows and cols because in the if we would be adding 1 to row and col

        # This way is more intuitive because we want to compare every diagonal and since we start at 0,0
        # We are checking the next row and column's diagonal to see if it matches.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True
