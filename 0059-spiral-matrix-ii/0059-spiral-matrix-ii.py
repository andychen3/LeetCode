class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] *n for i in range(n)]
        left, right, top, bottom = 0, n, 0, n
        num = 1
        while left < right and top < bottom:
            for i in range(left, right):
                mat[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bottom):
                mat[i][bottom-1] = num
                num += 1
            right -= 1
            
            for i in range(right - 1, left - 1, -1):
                mat[bottom-1][i] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                mat[i][left] = num
                num += 1
            left += 1
            
        return mat
                
                