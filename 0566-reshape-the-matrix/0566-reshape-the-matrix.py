class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if r*c != rows*cols:
            return mat
        
        ans = [[0]*c for _ in range(r)]
        
        for i in range(rows*cols):
            ans[i//c][i%c] = mat[i//cols][i%cols]
            
        return ans
                
            