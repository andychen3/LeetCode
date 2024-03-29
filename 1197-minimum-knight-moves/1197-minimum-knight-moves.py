from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0, 0, 0)])
        # directions = [(-1, -2), (-2,-1), (1,-2), (2,-1), (-2,1), (-1,2), (1,2), (2,1)]
        directions = [(-1,-2), (1,-2), (-1,2), (1, 2), (-2,-1), (-2,1), (2,-1), (2,1)]
        seen = {(0,0)}
        
        while queue:
            r, c, steps = queue.popleft()
            
            if (r, c) == (x, y):
                return steps
            
            for dx, dy in directions:
                new_dx, new_dy = dx + r, dy + c
                if (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))