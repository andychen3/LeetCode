class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        d = collections.deque()
        time = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    d.append((row,col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        while d and fresh_oranges > 0:
            
            for i in range(len(d)):
                r,c = d.popleft()
                for new_x, new_y in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_oranges -= 1
                        d.append((new_x,new_y))
            time += 1
                
        if fresh_oranges > 0:
            return -1
        return time
        