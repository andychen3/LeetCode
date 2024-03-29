class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != 1 or (x,y) in seen:
                return 0
            seen.add((x, y))
            ans = 1
            ans += dfs(x+1, y)
            ans += dfs(x-1, y)
            ans += dfs(x, y+1)
            ans += dfs(x, y-1)
            return ans
        
        seen = set()
        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in seen:
                    ans = max(ans, dfs(r,c))
        return ans