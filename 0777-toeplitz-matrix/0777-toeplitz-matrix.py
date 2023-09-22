from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        counts = defaultdict(set)

        for row in range(m):
            for col in range(n):
                counts[row-col].add(matrix[row][col])
        
        for values in counts.values():
            if len(values) > 1:
                return False
        return True
