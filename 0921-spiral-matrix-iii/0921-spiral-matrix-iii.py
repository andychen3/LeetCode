class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r, c = rows, cols
        ans = [[rStart, cStart]]
        directions = 1
        steps = 1

        while len(ans) < rows * cols:
            for _ in range(steps):
                cStart += directions
                if 0 <= cStart < c and 0 <= rStart < r:
                    ans.append([rStart, cStart])

            for _ in range(steps):
                rStart += directions
                if 0 <= cStart < c and 0 <= rStart < r:
                    ans.append([rStart, cStart])
            steps += 1
            directions *= -1
        return ans
