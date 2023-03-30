from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row = len(mat)
        col = len(mat[0])
        seen = set()
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col and mat[r][c] == 1
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c, 1))
                    seen.add((r,c))
                    
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
                    mat[new_x][new_y] = steps
        return mat