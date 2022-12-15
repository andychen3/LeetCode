class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        seen = set()
        row = len(grid)
        col = len(grid[0])
        
        def dfs(node):
            x, y = node
            
            for x1, y1 in ((0,1), (0,-1), (1,0), (-1,0)):
                new_x = x + x1
                new_y = y + y1
                
                if new_x < row and new_x >= 0 and new_y < col and new_y >= 0 and (new_x, new_y) not in seen:
                    if grid[new_x][new_y] == '1':
                        seen.add((new_x, new_y))
                        dfs((new_x, new_y))
        
        for rows in range(len(grid)):
            for cols in range(len(grid[0])):
                if grid[rows][cols] == '1' and (rows, cols) not in seen:
                    seen.add((rows, cols))
                    dfs((rows, cols))
                    islands += 1
        
        return islands
        