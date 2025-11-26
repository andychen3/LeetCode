from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 0
        
        queue = deque([[0, 0, 1]])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        seen = {(0, 0)}
        n = len(grid)

        while queue:
            row, col, steps = queue.popleft()

            if row == n - 1 and col == n - 1:
                return steps

            for dx, dy in directions:
                new_dx, new_dy = row + dx, col + dy

                if (new_dx, new_dy) not in seen and valid(new_dx, new_dy):
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        
        return -1