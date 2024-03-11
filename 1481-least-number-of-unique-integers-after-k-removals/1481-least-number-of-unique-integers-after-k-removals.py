from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values(), reverse=True)
        
        while k:
            val = freq[-1]
            if val <= k:
                k -= val
                freq.pop()
            else:
                break
        return len(freq)