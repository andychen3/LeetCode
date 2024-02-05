class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        seen = set()
        ans = 0
        
        
        def dfs(x, y):
            if x >= row or x < 0 or y >= col or y < 0 or grid[x][y] == "0" or (x, y) in seen:
                return
            # grid[x][y] = "0"
            seen.add((x, y))
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in seen:
                    ans += 1
                    dfs(r, c)
        return ans