from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        anti_diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        for row in range(m):
            for col in range(n):
                anti_diag[row + col].append(mat[row][col])
        
        ans = []
        for key, diag in anti_diag.items():
            if key % 2 == 0:
                ans += diag[::-1]
            else:
                ans += diag
        return ans
        