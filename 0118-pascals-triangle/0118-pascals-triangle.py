class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for row in range(1, numRows+1):
            r = [1] * row
            for i in range(1, len(r) - 1):
                r[i] = ans[-1][i-1] + ans[-1][i]
            ans.append(r)
        return ans