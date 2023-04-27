from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def check(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for x in [-1, 1]:
                    change = (x + num) % 10
                    ans.append(slots[:i] + str(change) + slots[i+1:])
            return ans
            
        
        
        if '0000' in deadends:
            return -1
        
        seen = set(deadends)
        seen.add('0000')
        d = deque([('0000', 0)])
        
        while d:
            slots, moves = d.popleft()
            if slots == target:
                return moves
            
            for neighbors in check(slots):
                if neighbors not in seen:
                    seen.add(neighbors)
                    d.append((neighbors, moves + 1))
        return -1