class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        
        mat = [[0]*col for _ in range(row)]
        
        for i in range(row*col):
            index = (i+k) % (row*col)
            mat[index//col][index%col] = grid[i//col][i%col]
        
        return mat