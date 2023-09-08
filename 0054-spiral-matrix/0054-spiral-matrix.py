class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns
        direction = 1  # 1 for right, -1 for left (initially start moving right)
        row, col = 0, -1  # Initialize starting position (0-based index)
        result = []  # List to store the elements in spiral order
        
        while rows * cols > 0:  # Continue until there are elements to process
            for _ in range(cols):  # Move horizontally
                col += direction
                result.append(matrix[row][col])
            rows -= 1  # Reduce the number of rows to process
            
            for _ in range(rows):  # Move vertically
                row += direction
                result.append(matrix[row][col])
            cols -= 1  # Reduce the number of columns to process
            
            direction *= -1  # Flip the direction for the next iteration
        
        return result
