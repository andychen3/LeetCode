class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        direction = [(0,1), (1,0), (-1,0), (0,-1)]
        ans = 0
        seen = set()
        
        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0 or (r,c) in seen:
                return 0
            
            seen.add((r,c))
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
    
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        return ans
        
            
            
            
            
            
            
        