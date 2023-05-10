class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top = 0
        bottom = n
        right = n
        left = 0
        nums = 1
        
        while left < right and top < bottom:
            # Move left to right
            for i in range(left, right):
                matrix[top][i] = nums
                nums += 1
            top += 1
            # top to bottom
            for i in range(top, bottom):
                matrix[i][right-1] = nums
                nums += 1
            right -= 1
            # Right to left
            
            # if not (left < right and top < bottom):
            #     break
            
            for i in range(right - 1, left - 1, -1):
                matrix[bottom - 1][i] = nums
                nums += 1
            bottom -= 1
            # bottom to top
            for i in range(bottom - 1, top - 1, -1):
                matrix[i][left] = nums
                nums += 1
            left += 1
        return matrix