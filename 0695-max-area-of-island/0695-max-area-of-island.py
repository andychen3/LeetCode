class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        max_area = 0
        
        def valid(row, col):
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1
        
        def dfs(x, y):
            area = 1
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    # area += 1
                    area += dfs(new_x, new_y)
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    max_area = max(dfs(r, c), max_area)
        return max_area
                    
                    