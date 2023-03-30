from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values(), reverse=True)
        i = 0
        
        while i < k:
            if freq[-1] + i <= k:
                i += freq[-1]
                freq.pop()
            else:
                break
        return len(freq)
            
        