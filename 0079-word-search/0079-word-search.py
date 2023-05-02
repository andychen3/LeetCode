class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        rows = len(board)
        cols = len(board[0])
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        
        def backtrack(char_set, index, coords):
            
            x, y = coords
            
            if index == len(word):
                return True
            for dx, dy in directions:
                new_dx, new_dy = dx + x, dy + y
                if valid(new_dx, new_dy) and board[new_dx][new_dy] == word[index] \
                and (new_dx,new_dy) not in char_set:
                    char_set.add((new_dx,new_dy))
                    if backtrack(char_set, index+1, (new_dx, new_dy)):
                        return True
                    char_set.remove((new_dx, new_dy))
            return False
    
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack({(r,c)}, 1, (r, c)):
                    return True
                    
                    
        return False
        
        
        
        
        