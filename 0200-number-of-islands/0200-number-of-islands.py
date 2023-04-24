class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1'
        
        rows = len(grid)
        cols = len(grid[0])
        
        seen = set()
        islands = 0
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def dfs(r, c):
            for dx, dy in directions:
                new_dx, new_dy = dx + r, dy + c
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    dfs(new_dx, new_dy)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r,c))
                    islands += 1
                    dfs(r, c)
        return islands