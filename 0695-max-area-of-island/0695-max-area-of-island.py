class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        ans = 0
        
        def dfs(x, y):
            ans = 0
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    ans += dfs(new_dx, new_dy) + 1
            return ans
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    ans = max(ans, dfs(r,c)+1)
                    
        return ans