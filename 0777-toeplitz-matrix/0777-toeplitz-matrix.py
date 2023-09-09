from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals = defaultdict(list)

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                diagonals[r - c].append(matrix[r][c])

        for _, values in diagonals.items():
            if not all(x == values[0] for x in values):
                return False
        return True
