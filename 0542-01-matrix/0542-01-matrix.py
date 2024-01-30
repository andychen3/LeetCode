from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        seen = set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        rows, cols = len(mat), len(mat[0])
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    mat[new_dx][new_dy] = steps
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        return mat