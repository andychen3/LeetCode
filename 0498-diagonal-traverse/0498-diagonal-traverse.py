from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        
        for r in range(rows):
            for c in range(cols):
                diagonals[r+c].append(mat[r][c])
                
        ans = []
        
        for key, values in diagonals.items():
            if key % 2 == 0:
                ans += values[::-1]
            else:
                ans += values
        return ans