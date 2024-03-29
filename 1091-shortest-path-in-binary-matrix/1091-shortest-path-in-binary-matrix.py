from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque([(0, 0, 1)])
        directions = [(0, 1), (1,0), (1,1), (0,-1), (-1,0), (-1,-1), (-1,1), (1,-1)]
        row, col = len(grid), len(grid[0])
        seen = {(0, 0)}
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 0
        
        while queue:
            x, y, steps = queue.popleft()
            
            if (x, y) == (row-1, col - 1) and grid[x][y] == 0:
                return steps
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        return -1
            