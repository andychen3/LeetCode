from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        seen = set()
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for c in range(n):
                if mat[i][c] == 0:
                    queue.append((i, c, 1))
                    seen.add((i, c))
        
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and mat[r][c] == 1

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_dx, new_dy = dx + row, dy + col
                if (new_dx, new_dy) not in seen and valid(new_dx, new_dy):
                    mat[new_dx][new_dy] = steps
                    seen.add((new_dx, new_dy))
                    queue.append((new_dx, new_dy, steps + 1))
        
        return mat