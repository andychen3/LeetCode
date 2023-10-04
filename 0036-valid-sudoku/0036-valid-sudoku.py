class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = set()
        row = set()
        col = set()
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] != '.':
                    if (board[r][c], r) in row:
                        return False
                    if (board[r][c], c) in col:
                        return False
                    if (board[r][c],(r//3)*3 + c//3 ) in boxes:
                        return False
                        
                    row.add((board[r][c], r))
                    col.add((board[r][c], c))
                    boxes.add((board[r][c],(r//3)*3 + c//3 ))
        return True
