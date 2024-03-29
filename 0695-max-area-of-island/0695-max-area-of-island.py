class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        def dfs(x, y):
            ans = 1
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    ans += dfs(new_dx, new_dy)
            return ans
            
        seen = set()
        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r,c))
                    ans = max(ans, dfs(r,c))
        return ans