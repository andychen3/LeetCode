from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        anti_diags = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            for c in range(cols):
                anti_diags[r + c].append(mat[r][c])

        ans = []
        for key, values in anti_diags.items():
            if key % 2 == 0:
                ans += values[::-1]
            else:
                ans += values
        return ans