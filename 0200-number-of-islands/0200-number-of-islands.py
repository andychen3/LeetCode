class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != "1" or (x,y) in seen:
                return
            seen.add((x,y))
            
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    ans += 1
                    dfs(row, col)
        return ans
                    