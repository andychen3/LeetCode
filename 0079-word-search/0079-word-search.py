class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def backtrack(row, col, i, seen):
            if i == len(word):
                return True
            
            for dx, dy in directions:
                new_dx, new_dy = row + dx, col + dy
                if valid(new_dx, new_dy) and (new_dx, new_dy) not in seen:
                    if board[new_dx][new_dy] == word[i]:
                        seen.add((new_dx, new_dy))
                        if backtrack(new_dx, new_dy, i+1, seen):
                            return True
                        seen.remove((new_dx, new_dy))
            return False
            
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False
        