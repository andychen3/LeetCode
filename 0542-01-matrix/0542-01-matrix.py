class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        q = deque()
        seen = set()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c, 1))
                    seen.add((r,c))
            
        while q:
            r, c, distance = q.popleft()
            for x, y in ((0,1), (0,-1), (1,0), (-1,0)):
                new_x = r + x
                new_y = c + y
                if new_x < rows and new_x >= 0 and new_y < cols and new_y >= 0 and (new_x, new_y) not in seen:
                    seen.add((new_x, new_y))
                    q.append((new_x, new_y, distance + 1))
                    mat[new_x][new_y] = distance

        return mat
            