class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        direction = 0
        res = []
        
        while left < right and top < bottom:
            if direction == 0:
                for i in range(left, right):
                    res.append(matrix[top][i])
                top += 1
            if direction == 1:
                for i in range(top, bottom):
                    res.append(matrix[i][right-1])
                right -= 1
            if direction == 2:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom-1][i])
                bottom -= 1
            if direction == 3:
                for i in range(bottom-1, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
            
        return res 
        