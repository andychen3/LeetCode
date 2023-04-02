class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < col
        
        
        rows = len(board)
        col = len(board[0])
        
        def backtrack(i, coord, seen):
            directions = ((0,1), (1,0), (-1,0), (0,-1))
            
            if i == len(word):
                return True
            x, y = coord
            
            for dx, dy in directions:
                new_x, new_y = dx + x, dy + y
                if valid(new_x, new_y) and (new_x, new_y) not in seen:
                    if board[new_x][new_y] == word[i]:
                        seen.add((new_x, new_y))
                        if backtrack(i+1, (new_x,new_y), seen):
                            return True
                        seen.remove((new_x,new_y))
            return False
            
        for r in range(rows):
            for c in range(col):
                if board[r][c] == word[0] and backtrack(1, (r,c), {(r,c)}):
                    return True
        return False