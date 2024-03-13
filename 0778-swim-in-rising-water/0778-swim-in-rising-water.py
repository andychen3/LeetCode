class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid)
        
        def check(k):
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            stack = [(0,0)]
            seen = {(0,0)}
            n = len(grid)
            
            while stack:
                x, y = stack.pop()
                
                if x == n - 1 and y == n - 1:
                    return True
                
                for dx, dy in directions:
                    new_dx, new_dy = dx + x, dy + y
                    if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                        if k >= grid[new_dx][new_dy]:
                            seen.add((new_dx, new_dy))
                            stack.append((new_dx, new_dy))
            return False
            
        left, right = grid[0][0], max(max(row) for row in grid)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left