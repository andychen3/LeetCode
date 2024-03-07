class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_set = set()
        atl_set = set()
        
        row, col = len(heights), len(heights[0])
        
        # DFS each call
        def dfs(x, y, seen, prev):
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in seen or heights[x][y] < prev:
                return
            seen.add((x, y))
            
            dfs(x+1, y, seen, heights[x][y])
            dfs(x-1, y, seen, heights[x][y])
            dfs(x, y+1, seen, heights[x][y])
            dfs(x, y-1, seen, heights[x][y])
        
        # Get Top and left
        for c in range(col):
            dfs(0, c, pac_set, -1)
            dfs(row - 1, c, atl_set, -1)
        
        # Get Bottom and Right
        for r in range(row):
            dfs(r, 0, pac_set, -1)
            dfs(r, col-1, atl_set, -1)
        
        # Return intersection of the sets
        return list(pac_set.intersection(atl_set))