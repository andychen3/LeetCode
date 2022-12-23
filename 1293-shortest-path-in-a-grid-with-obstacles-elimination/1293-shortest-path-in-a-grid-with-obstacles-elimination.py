from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        q = deque([(0,0,k)])
        seen = {(0,0,k)}
        steps = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def valid(row, col):
            return row < rows and row >= 0 and col < cols and col >= 0
        
        while q:
            q_len = len(q)
            
            for _ in range(q_len):
                x, y, obstacles = q.popleft()
                
                if (x, y) == (rows-1, cols-1):
                    return steps
                
                for r, c in directions:
                    new_x = x + r
                    new_y = y + c
                    
                    if valid(new_x, new_y):
                        
                        if grid[new_x][new_y] == 1 and obstacles > 0 and (new_x, new_y, obstacles-1) not in seen:
                            seen.add((new_x, new_y, obstacles-1))
                            q.append((new_x, new_y, obstacles-1))
                        elif grid[new_x][new_y] == 0 and (new_x, new_y, obstacles) not in seen:
                            seen.add((new_x, new_y, obstacles))
                            q.append((new_x, new_y, obstacles))
            steps += 1
        
        return -1
                            
                    
                    

                            
            