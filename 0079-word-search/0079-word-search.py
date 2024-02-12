class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def valid(x, y):
            return 0 <= x < row and 0 <= y < col
        
        def dfs(index, seen, x, y):
            if index == len(word):
                return True
            
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    if board[new_dx][new_dy] == word[index]:
                        seen.add((new_dx, new_dy))
                        if dfs(index + 1, seen, new_dx, new_dy):
                            return True
                        seen.remove((new_dx, new_dy))
            return False
            
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and dfs(1, {(r, c)}, r, c):
                    return True
        return False