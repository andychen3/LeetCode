class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
            res.append(1)
        return res