class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        rows = len(board)
        cols = len(board[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def backtrack(x, y, pos, seen):
            if pos == len(word):
                return True
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    if word[pos] == board[new_dx][new_dy]:
                        seen.add((new_dx, new_dy))
                        if backtrack(new_dx, new_dy, pos + 1, seen):
                            return True
                        seen.remove((new_dx, new_dy))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 1, {(r,c)}):
                    return True
        return False