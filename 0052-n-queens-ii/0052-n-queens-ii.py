class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, col, diagonal, anti_diagonal):
            if row == n:
                return 1
            
            solution = 0
            
            for cols in range(n):
                curr_diagonal = row - cols
                curr_anti_diagonal = row + cols
                if (cols in col or 
                    curr_diagonal in diagonal or 
                    curr_anti_diagonal in anti_diagonal):
                    continue
                
                col.add(cols)
                diagonal.add(curr_diagonal)
                anti_diagonal.add(curr_anti_diagonal)
                
                solution += backtrack(row+1, col, diagonal, anti_diagonal)
                
                col.remove(cols)
                diagonal.remove(curr_diagonal)
                anti_diagonal.remove(curr_anti_diagonal)
            
            return solution
                
                
                
        return backtrack(0, set(), set(), set())