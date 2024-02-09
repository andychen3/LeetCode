class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()
        n = len(board)
        
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".":
                    if (r, board[r][c]) in row_set:
                        return False
                    
                    if (c, board[r][c]) in col_set:
                        return False
                    
                    if (r//3, c//3, board[r][c]) in box_set:
                        return False
                    
                row_set.add((r, board[r][c]))
                col_set.add((c, board[r][c]))
                box_set.add((r//3, c//3, board[r][c]))
        return True
        