class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # MY assumptions are that i need row, col, and row // 3 and col //3 which will give me the box
        row_set = set()
        col_set = set()
        box_set = set()
        row, col = len(board), len(board[0])

        for r in range(row):
            for c in range(col):
                if board[r][c] != '.':
                    if (board[r][c], r) in row_set:
                        return False
                    if (board[r][c], c) in col_set:
                        return False
                    if (board[r][c], r//3, c//3) in box_set:
                        return False
                    
                    row_set.add((board[r][c], r))
                    col_set.add((board[r][c], c))
                    box_set.add((board[r][c], r//3, c//3))
        return True
