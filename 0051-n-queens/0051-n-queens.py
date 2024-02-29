class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r, col, diag, anti_diag):
            if r >= n:
                ans.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r-c) in diag or (r+c) in anti_diag:
                    continue
                
                col.add(c)
                diag.add(r-c)
                anti_diag.add(r+c)
                board[r][c] = "Q"
                backtrack(r + 1, col, diag, anti_diag)
            
                col.remove(c)
                diag.remove(r-c)
                anti_diag.remove(r+c)
                board[r][c] = "."
            
        ans = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set())
        return ans