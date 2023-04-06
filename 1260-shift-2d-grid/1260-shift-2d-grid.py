class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nRows, nCols = len(grid), len(grid[0])
        # k %= nRows * nCols
        if k == 0: return grid
        
        n = nRows * nCols
        arr = [0] * n
        for i in range(n):
            idx = (i + n - k) % n
            arr[i] = grid[idx // nCols][idx % nCols]
        
        for i in range(len(arr)):
            grid[i // nCols][i % nCols] = arr[i]
        return grid
#         row = len(grid)
#         col = len(grid[0])
        
#         N = row*col
        
#         res = [[0]*col for _ in range(row)]
        
#         for i in range(N):
#             j = (i+k)%N
#             res[j//col][j%col] = grid[i//col][i%col]
#         return res
                
        
        