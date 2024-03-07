class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        row, col = len(heights), len(heights[0])
        
        def dfs(x, y, seen, prev):
            if x < 0 or x >= row or y < 0 or y >= col or heights[x][y] < prev or (x,y) in seen:
                return
            seen.add((x, y))
            dfs(x+1, y, seen, heights[x][y])
            dfs(x-1, y, seen, heights[x][y])
            dfs(x, y+1, seen, heights[x][y])
            dfs(x, y-1, seen, heights[x][y])
            
        for r in range(row):
            dfs(r, 0, pac, -1)
            dfs(r, col - 1, atl, -1)
            
        for c in range(col):
            dfs(0, c, pac, -1)
            dfs(row - 1, c, atl, -1)
            
        return list(pac.intersection(atl))