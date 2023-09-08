class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # rows is for up and down or in short vertical
        # cols is for left and right or in short horizontal 

        rows, cols = len(matrix), len(matrix[0])
        directions = 1 # This is the value that we are going to use to iterate our col and row
        row, col = 0, -1 # we initialize 0 because we are starting horizontally first and that is why -1
        ans = []

        while rows * cols > 0:
            # Iterate horizontally
            for _ in range(cols):
                col += directions # we add to direction because directions is the iterator
                ans.append(matrix[row][col])
            
            # We do this and not cols first because after we move horizontally we 
            # have to go down. and to control how many times you can go down you take from rows
            rows -= 1 

            # Iterate vertically
            for _ in range(rows):
                row += directions
                ans.append(matrix[row][col])
            cols -= 1

            # Change direction
            directions *= -1
        
        return ans
            