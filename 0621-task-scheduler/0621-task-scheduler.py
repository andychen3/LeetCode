from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapify(max_heap)
        queue = deque()
        time = 0
        
        while max_heap or queue:
            time += 1
            
            if max_heap:
                count = heappop(max_heap) + 1
                if count:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                heappush(max_heap, queue.popleft()[0])
        return time
                