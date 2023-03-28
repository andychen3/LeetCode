class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and grid[r][c] == 1
        
        
        
        def dfs(x, y):
            ans = 1
            for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    ans += dfs(new_x, new_y)
            return ans
        
        
        row = len(grid)
        col = len(grid[0])
        seen = set()
        ans = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] and (r,c) not in seen:
                    seen.add((r,c))
                    ans = max(ans, dfs(r, c))
        return ans
                    