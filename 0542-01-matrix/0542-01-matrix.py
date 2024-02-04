from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = set()
        row, col = len(mat), len(mat[0])
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    seen.add((r,c))
                    queue.append((r, c, 1))
        
        def valid(r, c):
            return 0 <= r < row and 0 <= c < col
        
        while queue:
            x, y, steps = queue.popleft()
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    mat[new_dx][new_dy] = steps
                    queue.append((new_dx, new_dy, steps + 1))
        return mat
        