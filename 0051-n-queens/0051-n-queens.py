class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        col_set = set()
        diag_set = set()
        anti_diag_set = set()
        ans = []
        
        def backtrack(row):
            if row == n:
                ans.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                diagonal = row + col
                anti_diagonal = row - col
                
                if (diagonal in diag_set or anti_diagonal in anti_diag_set or col in col_set):
                    continue
                col_set.add(col)
                diag_set.add(diagonal)
                anti_diag_set.add(anti_diagonal)
                board[row][col] = 'Q'

                backtrack(row + 1)

                col_set.remove(col)
                diag_set.remove(diagonal)
                anti_diag_set.remove(anti_diagonal)
                board[row][col] = "."
                    
        backtrack(0)
        return ans
            
            
            