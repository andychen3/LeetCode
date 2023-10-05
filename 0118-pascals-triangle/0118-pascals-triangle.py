class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for row in range(numRows):
            new_row = [1] * (row+1)
            for j in range(1, len(new_row)-1):
                new_row[j] = ans[row-1][j-1] + ans[row-1][j]
            ans.append(new_row)
        return ans