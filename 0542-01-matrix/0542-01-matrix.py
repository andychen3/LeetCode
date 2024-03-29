from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        queue = deque()
        seen = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c, 1))
                    seen.add((r,c))
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and mat[x][y] == 1
            
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    mat[new_dx][new_dy] = steps
                    queue.append((new_dx, new_dy, steps + 1))
        return mat