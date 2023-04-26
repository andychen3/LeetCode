from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def change_lock(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for x in [-1, 1]:
                    change = (num+x) % 10
                    ans.append(node[:i] + str(change) + node[i+1:])
            return ans
            
        
        if '0000' in deadends:
            return -1
        
        seen = set(deadends)
        seen.add("0000")
        d = deque([('0000', 0)])
        
        while d:
            for _ in range(len(d)):
                node, steps = d.popleft()
                if node == target:
                    return steps
                
                for neighbor in change_lock(node):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        d.append((neighbor, steps+1))
        return -1
            
            
        
        
        