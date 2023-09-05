from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
            n = len(board)
            board.reverse() # We reverse the board so it's easier to access from bottom left

            def intToPos(square):
                # We subtract 1 from square to keep it 0 indexed
                r = (square - 1) // n
                c = (square - 1) % n
                if r % 2:
                    # Reason for this is because when odd you start from the rightmost column
                    c = n - 1 - c 
                    
                return [r, c]

            q = deque()
            q.append([1, 0]) # We start at 1 because the squares are labeled n to n^2
            visit = set()
            while q:
                square, moves = q.popleft()
                
                if square == n * n:
                    return moves

                # simulate 6 sided dice roll
                for i in range(1, 7):
                    nextSquare = square + i
                    r, c = intToPos(nextSquare)

                    # Check if the coordinates are within bounds
                    if 0 <= r < n and 0 <= c < n:
                        
                        # Check if the current square has a snake or ladder
                        if board[r][c] != -1:
                            nextSquare = board[r][c]

                        # Add the square onto the queue
                        if nextSquare not in visit:
                            visit.add(nextSquare)
                            q.append([nextSquare, moves + 1])
            return -1