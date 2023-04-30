class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        pacific_set = set()
        atlantic_set = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def dfs(x, y, visited):
            if (x,y) in visited:
                return
            visited.add((x,y))
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy):
                    if heights[new_dx][new_dy] >= heights[x][y]:
                        dfs(new_dx, new_dy, visited)
        
        for r in range(rows):
            dfs(r, 0, pacific_set)
            dfs(r, cols-1, atlantic_set)
        for c in range(cols):
            dfs(0, c, pacific_set)
            dfs(rows-1, c, atlantic_set)
            
        return list(pacific_set & atlantic_set)
        