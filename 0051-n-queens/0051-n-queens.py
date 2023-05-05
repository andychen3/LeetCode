class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        empty_board = [["."]*n for _ in range(n)]
        col_set = set()
        diag_set = set()
        anti_diag_set = set()
        ans = []
        
        def backtrack(row):
            if row == n:
                ans.append(["".join(empty_board[r]) for r in range(row)])
                return
                
            for col in range(n):
                if (col in col_set or (row-col) in diag_set or
                    (row + col) in anti_diag_set):    
                    continue
                
                col_set.add(col)
                diag_set.add(row-col)
                anti_diag_set.add(row+col)
                empty_board[row][col] = 'Q'
                
                backtrack(row + 1)
                
                col_set.remove(col)
                diag_set.remove(row-col)
                anti_diag_set.remove(row+col)
                empty_board[row][col] = '.'
        
        backtrack(0)     
        return ans
                    
                    
            
            