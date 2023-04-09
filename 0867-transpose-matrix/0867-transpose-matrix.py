class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        
        for c in range(col):
            levels = []
            for r in range(row):
                levels.append(matrix[r][c])
            ans.append(levels)
        
        return ans
                