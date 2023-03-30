class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows = len(matrix)
        columns = len(matrix[0])
        right = rows * columns - 1
        
        while left <= right:
            mid = (left+right) // 2
            row = mid // columns
            col = mid % columns
            number = matrix[row][col]
            
            if number == target:
                return True
            if number > target:
                right = mid -1
            else:
                left = mid + 1
        return False
        
        
        
        