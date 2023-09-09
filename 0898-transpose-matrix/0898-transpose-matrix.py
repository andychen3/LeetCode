class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = []
        # This way is faster with building an array within the for loops because its O(1) declaring an array
        # O(1) appending to array and appending to ans
        # The other way is to create a 2D matrix that is transposed and fill it in. But that is slower

        # We iterate with column first because when we transpose a matrix we switch rows with column
        for c in range(col):
            level = []
            for r in range(row):
                # This makes sense because when we access the r,c in the original matrix it is still
                # using its original structure.
                level.append(matrix[r][c])
            ans.append(level)
        return ans
        
        # Another answer is to do return [ans for ans in list(zip(*matrix))]