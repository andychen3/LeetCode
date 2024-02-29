import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        
        min_heap = list(counts.keys())
        heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]
            for i in range(first, first + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heappop(min_heap)
        return True