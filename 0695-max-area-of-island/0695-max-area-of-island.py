class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        
        def validate(r, c):
            return r < rows and r >= 0 and c < cols and c >= 0 and grid[r][c] == 1
        
        def dfs(x,y, tracker):
            for x1, y1 in ((0,1), (0,-1), (1,0), (-1,0)):
                new_x = x + x1
                new_y = y + y1
                if validate(new_x, new_y) and (new_x, new_y) not in seen:
                    tracker += 1
                    seen.add((new_x, new_y))
                    grid[new_x][new_y] = 0
                    tracker = dfs(new_x, new_y, tracker)
            return tracker
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    seen.add((r,c))
                    result = max(result, dfs(r, c, 1))
                    
        return result
            