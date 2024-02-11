from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    new_dx, new_dy = dx + x, dy + y
                    if valid(new_dx, new_dy):
                        grid[new_dx][new_dy] = 2
                        fresh -= 1
                        queue.append((new_dx, new_dy))
            minutes += 1
        return minutes if fresh == 0 else -1
                