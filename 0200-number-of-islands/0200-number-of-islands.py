class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        
        
        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != "1":
                return
            grid[x][y] = "0"
            
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
        return ans            
        
        