class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = 1 # it starts at one because we are building horizontally first
        # we start at 0 for x because we go through the first row first
        # We start y at -1 to make sure we are at the first index when we start
        x, y = 0, -1 
        ans = []

        while rows * cols > 0:
            for c in range(cols):
                y += directions
                ans.append(matrix[x][y])
            
            rows -= 1 # we decrement row because in a spiral after the first go row goes down 1

            for r in range(rows):
                x += directions
                ans.append(matrix[x][y])
            
            cols -= 1 # We decrement col after row because we start going horizontal again

            directions *= -1
        return ans