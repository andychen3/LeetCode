class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        ans = [[rStart, cStart]]
        steps = 1
        x, y = rStart, cStart
        
        while len(ans) < rows*cols:
            
            # right
            for _ in range(steps):
                x, y = x, y+1
                if valid(x, y):
                    ans.append([x,y])
                    
            # down
            for _ in range(steps):
                x, y = x+1, y
                if valid(x, y):
                    ans.append([x,y])
                    
            steps += 1
            
            # left
            
            for _ in range(steps):
                x, y = x, y-1
                if valid(x,y):
                    ans.append([x,y])
                    
            # up 
            for _ in range(steps):
                x, y = x-1, y
                if valid(x,y):
                    ans.append([x,y])
            
            steps += 1
        return ans