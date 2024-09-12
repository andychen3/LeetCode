from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        diag_dict = defaultdict(int)
        
        for r in range(row):
            for c in range(col):
                if (r - c) not in diag_dict:
                    diag_dict[r-c] = matrix[r][c]
                elif matrix[r][c] != diag_dict[r - c]:
                    return False
                
        return True