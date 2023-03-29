
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0,0,k,0)])
        seen = {(0,0,k)}
        row = len(grid)
        col = len(grid[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col
        
        while queue:
            x, y, remaining, steps = queue.popleft()
            
            if (x, y) == (row-1, col-1):
                return steps
            
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                
                if valid(new_x, new_y) and (new_x, new_y, remaining) not in seen:
                    if grid[new_x][new_y] == 0:
                        seen.add((new_x, new_y, remaining))
                        queue.append((new_x, new_y, remaining, steps + 1))
                    elif remaining and (new_x, new_y, remaining - 1) not in seen:
                        seen.add((new_x, new_y, remaining - 1))
                        queue.append((new_x, new_y, remaining - 1, steps + 1))
                        
        return -1
            
            