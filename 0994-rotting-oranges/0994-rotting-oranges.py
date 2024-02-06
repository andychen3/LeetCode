from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        fresh = 0
        queue = deque()
        row, col = len(grid), len(grid[0])
        minutes = -1
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r,c))
                else:
                    if grid[r][c] == 1:
                        fresh += 1
        
        if fresh == 0:
            return 0
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    new_dx, new_dy = dx + x, dy + y
                    if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                        grid[new_dx][new_dy] = 2
                        seen.add((new_dx, new_dy))
                        fresh -= 1
                        queue.append((new_dx, new_dy))
            minutes += 1

        
        return minutes if fresh == 0 else -1 