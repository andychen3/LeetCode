class Solution:
    def totalNQueens(self, n: int) -> int:
        # The trick is you can make sure a queen is not attacked by checking if
        # They are in the same row, col, diagonal, or anti diagonal
        # A way to check diagonal is row - col and to check anti diagonal is row + col
        # Backtrack because of time complexity

        def backtrack(row, column, diagonal, anti_diagonal):
            if row == n:
                return 1

            ans = 0
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                # Check if they are in the same row, col, diagonal, or anti_diagonal
                if (col in column or curr_diagonal in diagonal or 
                    curr_anti_diagonal in anti_diagonal):
                    continue
                
                # Add them all to set so easy O(1) check to see if next queen placement
                # is valid
                column.add(col)
                diagonal.add(curr_diagonal)
                anti_diagonal.add(curr_anti_diagonal)

                # Call backtrack and add to the answer
                ans += backtrack(row + 1, column, diagonal, anti_diagonal)

                # Remove state when backtrack comes back to check other possibilities
                column.remove(col)
                diagonal.remove(curr_diagonal)
                anti_diagonal.remove(curr_anti_diagonal)
            
            return ans

        return backtrack(0, set(), set(), set())


