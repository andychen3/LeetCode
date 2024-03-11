from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        ans = []
        
        for chars in order:
            if chars in counts:
                ans.append(chars * counts[chars])
                del counts[chars]
                
        for key, val in counts.items():
            ans.append(key * val)
        
        return "".join(ans)
