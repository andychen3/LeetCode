class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        atl, pac = set(), set()
        
        def dfs(x, y, seen, prev):
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in seen or heights[x][y] < prev:
                return
            seen.add((x, y))
            dfs(x+1, y, seen, heights[x][y])
            dfs(x-1, y, seen, heights[x][y])
            dfs(x, y+1, seen, heights[x][y])
            dfs(x, y-1, seen, heights[x][y])
        
        for i in range(col):
            dfs(0, i, pac, -1)
            dfs(row - 1, i, atl, -1)
            
        for j in range(row):
            dfs(j, 0, pac, -1)
            dfs(j, col - 1, atl, -1)
        
        return list(atl & pac)