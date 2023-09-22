class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = 1 # it starts at one because we are building horizontally first
        x, y = 0, -1
        ans = []

        while rows * cols > 0:
            for c in range(cols):
                y += directions
                ans.append(matrix[x][y])
            
            rows -= 1

            for r in range(rows):
                x += directions
                ans.append(matrix[x][y])
            
            cols -= 1

            directions *= -1
        return ans