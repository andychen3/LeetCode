class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        ans = 0
        
        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == '0' or (x, y) in seen:
                return
            seen.add((x,y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs(r,c)
                    ans += 1
        return ans