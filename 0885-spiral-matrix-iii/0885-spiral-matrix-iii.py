class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        coordinates = [[rStart, cStart]]
        steps = 1
        x, y = rStart, cStart
    
        
        while len(coordinates) < rows*cols:
            
            for _ in range(steps):
                x, y = x, y+1
                if valid(x, y):
                    coordinates.append([x,y])
                    
            for _ in range(steps):
                x, y = x+1, y
                if valid(x, y):
                    coordinates.append([x,y])
            
            steps += 1
            
            for _ in range(steps):
                x, y = x, y-1
                if valid(x, y):
                    coordinates.append([x,y])
            
            for _ in range(steps):
                x, y = x-1, y
                if valid(x, y):
                    coordinates.append([x,y])
            
            steps += 1
            
        return coordinates
        
        