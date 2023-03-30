import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        
        for key, vals in counter.items():
            heappush(heap, (-vals, key))
        
        return [heappop(heap)[1] for _ in range(k)]
            