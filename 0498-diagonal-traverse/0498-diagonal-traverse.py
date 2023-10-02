from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag = defaultdict(list)
        row, col = len(mat), len(mat[0])

        for r in range(row):
            for c in range(col):
                diag[r+c].append(mat[r][c])
        
        ans = []

        for key, val in diag.items():
            if key % 2 == 0:
                ans += val[::-1]
            else:
                ans += val
        return ans
