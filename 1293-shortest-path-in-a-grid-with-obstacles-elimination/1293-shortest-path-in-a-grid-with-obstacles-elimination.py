from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, k)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = {(0, 0, k)}

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n

        while queue:
            row, col, steps, removals = queue.popleft()

            if (row, col) == (m - 1, n - 1) and removals >= 0:
                return steps

            for dx, dy in directions:
                new_dx, new_dy = row + dx, col + dy

                if valid(new_dx, new_dy): 
                    if grid[new_dx][new_dy] == 1 and removals - 1 >= 0 and (new_dx, new_dy, removals - 1) not in seen:
                        seen.add((new_dx, new_dy, removals - 1))
                        queue.append((new_dx, new_dy, steps + 1, removals - 1))
                    elif grid[new_dx][new_dy] == 0 and (new_dx, new_dy, removals) not in seen:
                        seen.add((new_dx, new_dy, removals))
                        queue.append((new_dx, new_dy, steps + 1, removals))
                    
        return -1
