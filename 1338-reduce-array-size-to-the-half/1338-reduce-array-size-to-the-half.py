from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values())
        half = len(arr) // 2
        total = len(arr)
        ans = 0
        
        while total > half:
            total -= freq[-1]
            freq.pop()
            ans += 1
        
        return ans
        