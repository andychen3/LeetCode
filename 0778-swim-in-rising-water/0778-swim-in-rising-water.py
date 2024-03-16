import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = {(0,0)}
        
        while heap:
            time, x, y = heappop(heap)
            
            if x == n - 1 and y == n - 1:
                return time
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if 0 <= new_dx < n and 0 <= new_dy < n and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    heappush(heap, (max(time, grid[new_dx][new_dy]), new_dx, new_dy))
        
            
            