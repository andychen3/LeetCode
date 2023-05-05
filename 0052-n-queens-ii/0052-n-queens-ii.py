class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]
        col_set = set()
        diag_set = set()
        anti_diag_set = set()
        res = 0
        
        def backtrack(row):
            nonlocal res
            if row == n:
                res += 1
                return
            
            for col in range(n):
                if (col in col_set or (row-col) in diag_set
                   or (row + col) in anti_diag_set):
                    continue
                
                col_set.add(col)
                diag_set.add(row-col)
                anti_diag_set.add(row+col)
                board[row][col] = 'Q'
                
                backtrack(row+1)
                
                col_set.remove(col)
                diag_set.remove(row-col)
                anti_diag_set.remove(row+col)
                board[row][col] = '.'
                
        backtrack(0)
        return res