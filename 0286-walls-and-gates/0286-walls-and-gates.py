from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        d = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        seen = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        # collect all the gates
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    d.append((r, c, 0))
                    seen.add((r,c))
        
        def valid(r,c):
            return 0 <= r < rows and 0 <= c < cols and rooms[r][c] != -1
        # Go through deque and expand out
        
        while d:
            x, y, steps = d.popleft()
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    min_val = min(rooms[new_dx][new_dy], steps+1)
                    rooms[new_dx][new_dy] = min_val
                    d.append((new_dx, new_dy, steps + 1))
        return rooms