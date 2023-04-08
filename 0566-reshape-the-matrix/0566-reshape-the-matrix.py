class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if r*c != row*col:
            return mat
        
        grid = [[0]*c for _ in range(r)]
        
        for i in range(row*col):
            grid[i//c][i%c] = mat[i//col][i%col]
        
        return grid