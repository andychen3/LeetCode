class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        
        for c in range(col):
            level = []
            for r in range(row):
                level.append(matrix[r][c])
            res.append(level)
        return res
        