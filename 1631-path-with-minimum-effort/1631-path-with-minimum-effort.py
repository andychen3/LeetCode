class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def check(effort, x, y):
            directions = ((0,1), (1,0), (-1,0), (0,-1))
            
            
            if (x,y) == (rows-1, cols -1):
                return True
            
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    if abs(heights[new_x][new_y] - heights[x][y]) <= effort:
                        seen.add((new_x, new_y))
                        if check(effort, new_x, new_y):
                            return True
            return False
        

        rows = len(heights)
        cols = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        
        while left <= right:
            seen = {(0,0)}
            mid = (left+right) // 2
            if check(mid, 0,0):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        
        
        
        
        
        