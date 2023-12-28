from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = dict(sorted(Counter(s).items() ,key=lambda x:x[1], reverse=True))
        print(counts)
        ans = []
        
        for key, val in counts.items():
            ans.append(key * val)
        
        return "".join(ans)