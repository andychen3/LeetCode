from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows, cols = len(mat), len(mat[0])
        seen = set()
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        while queue:
            x, y, steps = queue.popleft()
            
            for x1, y1 in [(0, 1), (1, 0), (-1,0), (0,-1)]:
                new_dx, new_dy = x1 + x, y1 + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps+1))
                    mat[new_dx][new_dy] = steps
        return mat
                