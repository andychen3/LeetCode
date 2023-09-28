class Solution:
    def judgeCircle(self, moves: str) -> bool:
        origin = (0,0)
        row, col = (0,0)
        for directions in moves:
            if directions == "U":
                row -= 1
            elif directions == "D":
                row += 1
            elif directions == "L":
                col += 1
            else:
                col -= 1
        
        if (row, col) == origin:
                return True
        return False