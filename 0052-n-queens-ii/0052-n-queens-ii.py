class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, col_set, diag_set, anti_diag_set):
            if row == n:
                return 1
            
            result = 0
            
            for col in range(n):
                if col in col_set or (row - col) in diag_set or (row + col) in anti_diag_set:
                    continue
                    
                col_set.add(col)
                diag_set.add(row-col)
                anti_diag_set.add(row+col)
                
                result += backtrack(row + 1, col_set, diag_set, anti_diag_set)
                col_set.remove(col)
                diag_set.remove(row-col)
                anti_diag_set.remove(row+col)
            return result
        
        return backtrack(0, set(), set(), set())
                