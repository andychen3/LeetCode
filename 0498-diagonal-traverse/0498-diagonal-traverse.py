from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        rows = len(mat)
        col = len(mat[0])
        
        for r in range(rows):
            for c in range(col):
                diagonals[r+c].append(mat[r][c])
                
        ans = []
        
        for key, vals in diagonals.items():
            if key % 2 == 0:
                ans += vals[::-1]
            else:
                ans += vals
        
        return ans
        