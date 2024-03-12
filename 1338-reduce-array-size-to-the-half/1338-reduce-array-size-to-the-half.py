from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        freq = sorted(counts.values())
        ans = 0
        n = len(arr)
        
        while n > len(arr) / 2:
            n -= freq[-1]
            freq.pop()
            ans += 1
        return ans
        