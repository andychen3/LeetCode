class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        M = row*col
        left = 0
        right = M - 1
        
        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col
            num = matrix[r][c]
            if num == target:
                return True
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
            