class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and grid[r][c] == "1"
        
        
        def dfs(x, y):
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    dfs(new_x, new_y)
        
        row = len(grid)
        col = len(grid[0])
        seen = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        ans = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in seen:
                    ans += 1
                    seen.add((r,c))
                    dfs(r,c)
        return ans
                    