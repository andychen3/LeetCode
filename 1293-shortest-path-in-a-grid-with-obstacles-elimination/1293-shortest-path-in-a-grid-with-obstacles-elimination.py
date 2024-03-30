from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0,0,0,k)])
        seen = {(0,0,k)}
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        row, col = len(grid), len(grid[0])
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col
        
        while queue:
            x, y, steps, remain = queue.popleft()
            
            if (x, y) == (row-1,col-1):
                return steps
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy):
                    if grid[new_dx][new_dy] == 0 and (new_dx, new_dy, remain) not in seen:
                        seen.add((new_dx, new_dy, remain))
                        queue.append((new_dx, new_dy, steps + 1, remain))
                    elif grid[new_dx][new_dy] and remain > 0 and (new_dx, new_dy, remain-1) not in seen:
                        seen.add((new_dx, new_dy, remain - 1))
                        queue.append((new_dx, new_dy, steps + 1, remain-1))
        return -1
                        