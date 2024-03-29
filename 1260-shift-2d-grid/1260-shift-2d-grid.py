class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        
        ans = [[0]*col for _ in range(row)]
        
        for i in range(row*col):
            index = (i + k) % (row*col)
            ans[index // col][index % col] = grid[i // col][i % col]
        return ans
        