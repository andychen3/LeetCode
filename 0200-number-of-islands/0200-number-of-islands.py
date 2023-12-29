class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        ans = 0
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"
        
        
        def dfs(x, y):
            for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    dfs(new_dx, new_dy)
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1
                    dfs(row, col)
        return ans