from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        seen = {start}
        
        while queue:
            node = queue.popleft()
            
            if arr[node] == 0:
                return True
            
            for neighbor in [node + arr[node], node - arr[node]]:
                if 0 <= neighbor < len(arr) and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False
            