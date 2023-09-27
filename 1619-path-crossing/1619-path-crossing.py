class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0,0)}
        row, col = 0, 0
        for directions in path:
            if directions == 'N':
                row -= 1
            elif directions == 'S':
                row += 1
            elif directions == 'W':
                col += 1
            else:
                col -= 1
            if (row, col) in seen:
                return True
            seen.add((row,col))
        return False
