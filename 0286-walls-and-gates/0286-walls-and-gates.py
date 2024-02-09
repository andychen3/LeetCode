from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        row, col = len(rooms), len(rooms[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = set()
        
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    queue.append((r, c, 1))
                    seen.add((r,c))
            
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and rooms[r][c] != -1
            
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    rooms[new_dx][new_dy] = min(steps, rooms[new_dx][new_dy])
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        return rooms