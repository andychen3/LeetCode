from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-vals for vals in freq.values()]
        heapify(heap)
        q = deque()
        time = 0
        
        while heap or q:
            time += 1
            if heap:
                count = 1 + heappop(heap)
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        return time
            
        
        
        