from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # it can potentially be greedy because it asks for min size.
        # Also because you can kind of tell that the most optimal solution will probably
        # come from deleting the number that has the most occurences
        n = len(arr) // 2
        counts = Counter(arr)
        freq = sorted(counts.values())
        ans = 0
        
        while n > 0:
            val = freq[-1]
            n -= val
            freq.pop()
            ans += 1

        return ans
            