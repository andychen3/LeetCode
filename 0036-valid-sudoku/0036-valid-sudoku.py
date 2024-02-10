class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        box_set = set()
        
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if (board[row][col], row) in row_set:
                        return False
                    if (board[row][col], col) in col_set:
                        return False
                    if (board[row][col], row//3, col//3) in box_set:
                        return False
                    
                row_set.add((board[row][col], row))
                col_set.add((board[row][col], col))
                box_set.add((board[row][col], row//3, col//3))
        return True