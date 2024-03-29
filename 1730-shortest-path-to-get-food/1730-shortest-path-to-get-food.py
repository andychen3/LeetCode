from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and (grid[x][y] == "O" or grid[x][y] == "#")
        
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "*":
                    queue.append((r, c, 0))
                    seen.add((r, c))
                    break
        
        while queue:
            x, y, steps = queue.popleft()
            
            if grid[x][y] == "#":
                return steps
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        return -1