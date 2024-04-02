from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        fresh = 0
        seen = set()
        queue = deque()
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and grid[x][y] == 1
        
        time = 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_dx, new_dy = dx + x, dy + y
                    if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                        fresh -= 1
                        seen.add((new_dx, new_dy))
                        queue.append((new_dx, new_dy))
            time += 1
        
        return time if fresh == 0 else -1
                        
                        
                        
                        
                        
            