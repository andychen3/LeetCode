class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        
        N = row*col
        
        res = [[0]*col for _ in range(row)]
        
        for i in range(N):
            j = (i+k)%N
            res[j//col][j%col] = grid[i//col][i%col]
        return res
                
        
        