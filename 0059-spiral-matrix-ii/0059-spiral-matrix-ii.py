class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        rows, cols = n, n
        directions = 1
        x, y = 0, -1
        num = 1

        while rows * cols > 0:
            for c in range(cols):
                y += directions
                ans[x][y] = num
                num += 1
            
            rows -= 1

            for r in range(rows):
                x += directions
                ans[x][y] = num
                num += 1
            cols -= 1

            directions *= -1
        return ans