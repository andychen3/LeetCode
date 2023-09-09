class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []

        for c in range(cols):
            levels = []
            for r in range(rows):
                levels.append(matrix[r][c])
            ans.append(levels)
        return ans
        