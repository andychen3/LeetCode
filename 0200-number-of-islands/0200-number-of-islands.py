class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        seen = set()
        res = 0

        def valid(dx, dy):
            return dx < row and dy < col and dx >= 0 and dy >= 0 and grid[dx][dy] == '1' 

        def dfs(r, c):
            seen.add((r, c))

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_dx, new_dy = dx + r, dy + c
                if (new_dx, new_dy) not in seen and valid(new_dx, new_dy):
                    dfs(new_dx, new_dy)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in seen:
                    res += 1
                    dfs(i, j)

        return res