from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        odds = 0
        
        for freq in counts.values():
            if freq % 2 == 1:
                odds += 1
        
        if odds > 1:
            return len(s) - odds + 1
        return len(s)