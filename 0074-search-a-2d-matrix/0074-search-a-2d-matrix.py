class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col
            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False     