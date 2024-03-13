from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        anti_diagonals = defaultdict(list)
        
        m, n = len(mat), len(mat[0])
        
        for row in range(m):
            for col in range(n):
                anti_diagonals[row + col].append(mat[row][col])
                
                
        ans = []
        
        for key, val in anti_diagonals.items():
            if key % 2 == 0:
                ans += val[::-1]
            else:
                ans += val
        return ans