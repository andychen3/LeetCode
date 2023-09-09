class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = 1
        row, col = 0, -1
        ans = []

        while rows * cols > 0:
            for _ in range(cols):
                col += directions
                ans.append(matrix[row][col])
            
            rows -= 1

            for _ in range(rows):
                row += directions
                ans.append(matrix[row][col])
            cols -= 1

            directions *= -1
        return ans