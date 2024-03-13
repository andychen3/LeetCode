from collections import defaultdict
import heapq
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diag = defaultdict(list)
        m, n = len(mat), len(mat[0])
        
        for row in range(m):
            for col in range(n):
                diag[row - col].append(mat[row][col])
                
        for key, vals in diag.items():
            diag[key] = sorted(vals, reverse=True)
            
        for row in range(m):
            for col in range(n):
                val = diag[row-col].pop()
                mat[row][col] = val
        return mat