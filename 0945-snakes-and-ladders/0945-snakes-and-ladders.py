from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
            n = len(board)
            board.reverse()

            def intToPos(square):
                r = (square - 1) // n
                c = (square - 1) % n
                if r % 2:
                    c = n - 1 - c
                    
                return [r, c]

            q = deque()
            q.append([1, 0]) 
            visit = set()
            while q:
                square, moves = q.popleft()
                if square == n * n:
                    return moves

                for i in range(1, 7):
                    nextSquare = square + i
                    r, c = intToPos(nextSquare)

                    # if r < 0 or r >= n or c < 0 or c >= n:
                    #     continue
                    if 0 <= r < n and 0 <= c < n:

                        if board[r][c] != -1:
                            nextSquare = board[r][c]

                        if nextSquare not in visit:
                            visit.add(nextSquare)
                            q.append([nextSquare, moves + 1])
            return -1