class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(x, y):
            return x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] == '1'
        
        
        def dfs(x, y):
            for x1, y1 in directions:
                new_x = x + x1
                new_y = y + y1
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    dfs(new_x, new_y)
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    ans += 1
                    dfs(r,c)
                    
        return ans
                    
        