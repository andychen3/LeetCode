from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count("R")
        d_count = len(senate) - r_count

        d_ban = 0
        r_ban = 0

        queue = deque(senate)

        while r_count and d_count:
            curr = queue.popleft()

            if curr == "R":
                if r_ban:
                    r_ban -= 1
                    r_count -= 1
                else:
                    d_ban += 1
                    queue.append("R")
            else:  
                if d_ban:
                    d_ban -= 1
                    d_count -= 1
                else:
                    r_ban += 1
                    queue.append("D")
        
        return "Dire" if d_count else "Radiant"