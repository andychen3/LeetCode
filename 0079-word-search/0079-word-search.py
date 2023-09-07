class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # The reason you can identify that this problem is a candidate for backtracking is because
        # It involes search pruning for an answer. And the time complexity

        row = len(board)
        col = len(board[0])

        def valid(r, c):
            return 0 <= r < row and 0 <= c < col

        def backtrack(x, y, index, seen):
            # Since it's backtrack we need a base case
            if index == len(word):
                return True
            
            directions = ((0,1), (1,0), (-1,0), (0,-1))

            for dx, dy in directions:
                next_row, next_col = dx + x, dy + y
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    # Check if the next coordinate is the next word
                    if board[next_row][next_col] == word[index]:
                        seen.add((next_row, next_col))
                        # We backtrack to explore the next option and if it comes back true
                        # means we found the answer. If not it keeps searching
                        if backtrack(next_row, next_col, index + 1, seen):
                            return True
                        seen.remove((next_row, next_col))
            return False




        
        # Traverse the graph
        for i in range(row):
            for j in range(col):
                # We only check if we find the first letter of word. We also pass 1
                # because we are looking for the second char
                if board[i][j] == word[0] and backtrack(i, j, 1, {(i, j)}):
                    return True
        
        return False