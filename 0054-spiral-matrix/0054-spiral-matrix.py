class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = 1
        x, y = 0, -1
        row, col = len(matrix), len(matrix[0])
        ans = []
        
        while row * col > 0:
            for _ in range(col):
                y += directions
                ans.append(matrix[x][y])
            
            row -= 1
            
            for _ in range(row):
                x += directions
                ans.append(matrix[x][y])
            
            col -= 1
            directions *= -1
        return ans