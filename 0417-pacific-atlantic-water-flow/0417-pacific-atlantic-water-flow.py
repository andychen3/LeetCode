class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        rows = len(heights)
        cols = len(heights[0])
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        
        def dfs(r, c, visited):
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            
            for dx, dy in directions:
                new_dx, new_dy = dx + r, dy + c
                if valid(new_dx, new_dy):
                    if heights[new_dx][new_dy] >= heights[r][c]:
                        dfs(new_dx, new_dy, visited)
        
        
        # iterate through rows and cols to get the borders
        for r in range(rows):
            dfs(r, 0, pacific_set)
            dfs(r, cols-1, atlantic_set)
        for c in range(cols):
            dfs(0, c, pacific_set)
            dfs(rows-1, c, atlantic_set)
        
        return list(pacific_set & atlantic_set)