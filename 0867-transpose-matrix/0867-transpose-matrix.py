class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for r in range(len(matrix[0])):
            level = []
            for c in range(len(matrix)):
                level.append(matrix[c][r])
            ans.append(level)
        return ans