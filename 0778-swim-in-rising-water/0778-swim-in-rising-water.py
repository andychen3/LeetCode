import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        heap = [(grid[0][0], 0, 0)]
        seen = {(0,0)}
        n = len(grid)
        
        while heap:
            time, row, col = heappop(heap)
            
            if row == n-1 and col == n - 1:
                return time
            
            for dx, dy in directions:
                new_dx, new_dy = dx + row, dy + col
                if 0 <= new_dx < n and 0 <= new_dy < n and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    heappush(heap, (max(time, grid[new_dx][new_dy]), new_dx, new_dy))
        