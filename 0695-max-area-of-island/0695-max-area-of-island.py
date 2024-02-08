class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        ans = 0
        seen = set()
        
        # def valid(x, y):
        #     return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r,c) in seen:
                return 0
            
            seen.add((r,c))
            area = 1
        
            area += dfs(r-1, c) 
            area += dfs(r+1, c)
            area += dfs(r, c-1)
            area += dfs(r, c+1)
            return area
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        return ans
        
            
            
            
            
            
            
        