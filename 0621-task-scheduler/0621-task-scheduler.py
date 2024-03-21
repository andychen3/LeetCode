from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-freq for freq in counts.values()]
        heapify(heap)
        time = 0
        queue = deque()
        
        while queue or heap:
            time += 1
            
            if heap:
                count = heappop(heap) + 1
                if count:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                heappush(heap, queue.popleft()[0])
        return time