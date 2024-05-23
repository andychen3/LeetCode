class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        directions = 1
        ans = []
        x, y = 0, -1
        
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
        
        
        
        
        
        # Time 
        # O(N^2)
        # Space
        # O(N)