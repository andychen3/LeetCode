class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = 1
        row, col = 0, -1
        ans = []
        m = len(matrix)
        n = len(matrix[0])

        while m * n > 0:
            for _ in range(n):
                col += directions
                ans.append(matrix[row][col])
            m -= 1

            for _ in range(m):
                row += directions
                ans.append(matrix[row][col])
            n -= 1
            directions *= -1
        return ans
