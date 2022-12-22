from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def valid(rows, cols):
            return rows < N and rows >= 0 and cols < col and cols >= 0 and grid[rows][cols] == 0
        
        N = len(grid)
        col = len(grid[0])
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        
        q = deque([(0,0,1)])
        seen = {(0,0)}
        directions = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1))
        
        while q:
            x, y, steps = q.popleft()
            
            if (x, y) == (N-1, N-1):
                    return steps
            
            for x1, y1 in directions:
                new_x = x + x1
                new_y = y + y1

                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    q.append((new_x, new_y, steps+1))
                
        return -1
            
            
       