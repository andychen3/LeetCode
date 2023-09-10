class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = [[rStart, cStart]] # We add this in because we include our starting position
        directions = 1 # Direction starts at one because we start horizontally left to right
        # we have steps because we go out of bounds. so the pattern is 1, 2,2, 3,3,3, ...etc
        # That is why we don't use row and cols for the for loops compared to the other spiral matrix
        # problems
        steps = 1 

        # The reason it's len(ans) < then row * cols instead of row * cols > 0 
        # is because we don't decrement rows and cols. And you can never have more len(ans) then row*cols
        while len(ans) < rows * cols: 
            for _ in range(steps):
                cStart += directions
                # To make sure to only append points that are within bounds since we traverse out of bounds
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    ans.append([rStart, cStart])

            for _ in range(steps):
                rStart += directions
                if 0 <= cStart < cols and 0 <= rStart < rows:
                    ans.append([rStart, cStart])
            steps += 1
            directions *= -1
        return ans
