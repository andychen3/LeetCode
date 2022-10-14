from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        rows, cols = len(grid), len(grid[0])
        stack = []
    
        
        def dfs():
            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for new_x, new_y in ((x-1,y), (x+1,y), (x,y+1), (x,y-1)):
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
                        stack.append((new_x,new_y))
                        grid[new_x][new_y] == '0'
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    stack.append((row,col))
                    dfs()
                    num_islands += 1
        
        return num_islands
                    
        
            
        
        
        
            
        
        
        
        
        
        
        
#         def search(d):
#             while d:
#                 r, c = d.popleft()
#                 grid[r][c] = '0'
                
#                 for new_x, new_y in (r-1,c), (r+1,c), (r,c-1), (r,c+1):
#                     if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == '1':
#                         grid[new_x][new_y] = '0'
#                         d.append((new_x,new_y))
        
#         num_islands = 0
#         d = deque()
        
#         rows = len(grid)
#         cols = len(grid[0])
        
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == '1':
#                     d.append((row,col))
#                     search(d)
#                     num_islands += 1
        
#         return num_islands
            
            
        
            