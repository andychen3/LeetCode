class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows = cols = n
        directions = 1
        row, col = 0, -1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        nums = 1

        while rows * cols > 0:
            for _ in range(cols):
                col += directions
                ans[row][col] = nums
                nums += 1
            
            rows -= 1
            
            for _ in range(rows):
                row += directions
                ans[row][col] = nums
                nums += 1
            
            cols -= 1
            
            directions *= -1
        return ans

