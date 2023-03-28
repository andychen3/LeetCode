from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and grid[r][c] == 0
        
        
        row = len(grid)
        col = len(grid[0])
        queue = deque([(0,0,1)])
        directions = ((0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1))
        seen = set()
        
        while queue:
            queue_len = len(queue)
            
            for _ in range(queue_len):
                x, y, steps = queue.popleft()
                
                if (x, y) == (row-1, col-1):
                    return steps
                
                for dx, dy in directions:
                    new_x, new_y = dx + x, dy + y
                    if valid(new_x, new_y) and (new_x, new_y) not in seen:
                        seen.add((new_x, new_y))
                        queue.append((new_x, new_y, steps+1))
                        
        return -1
                        
        
        
        