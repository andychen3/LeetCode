from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        
        def dfs(x, y):
            if 0 > x  or x >= rows or 0 > y or y >= cols:
                return
            if grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            
#             dfs(x+1, y)
#             dfs(x-1, y)
#             dfs(x, y+1)
#             dfs(x, y-1)
            
            [dfs(x + x1, y + y1) for x1, y1 in ((1,0), (-1,0), (0,1), (0,-1))]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans
        
        
        

            
            
        
            