from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and maze[r][c] == '.'
        
        row = len(maze)
        col = len(maze[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        start_x, start_y = entrance
        queue = deque([(start_x, start_y, 0)])
        seen = {(start_x, start_y)}
        
        while queue:
            x, y, steps = queue.popleft()
            
            if [x,y] != entrance:
                if x == 0 or x == row-1 or y == 0 or y == col-1:
                    return steps
            
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
                    
        return -1
        