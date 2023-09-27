from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1
        
        freq = counts.values()

        return len(set(freq)) == 1
        