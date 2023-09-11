from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = deque()
        seen = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        

        while queue:
            x, y = queue.popleft()

            # Change all rows into zero
            for i in range(rows):
                matrix[i][y] = 0
                seen.add((i, y))
            
            # Change all cols into zero:
            for i in range(cols):
                matrix[x][i] = 0
                seen.add((x, i))
        return matrix

