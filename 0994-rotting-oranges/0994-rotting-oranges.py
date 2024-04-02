from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh_oranges = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        queue = deque()
        seen = set()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    fresh_oranges += 1

        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        time = 0
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_dx, new_dy = dx + x, dy + y
                    if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                        fresh_oranges -= 1
                        seen.add((new_dx, new_dy))
                        queue.append((new_dx, new_dy))
            
            time += 1
        
        return time if fresh_oranges == 0 else -1