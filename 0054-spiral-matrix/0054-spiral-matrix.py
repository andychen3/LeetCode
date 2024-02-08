class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 1
        x, y = 0, -1
        ans = []
        row, col = len(matrix), len(matrix[0])
        
        while row * col > 0:
            for _ in range(col):
                y += direction
                ans.append(matrix[x][y])
            
            row -= 1
            
            for _ in range(row):
                x += direction
                ans.append(matrix[x][y])
                
            col -= 1
            direction *= -1
        return ans