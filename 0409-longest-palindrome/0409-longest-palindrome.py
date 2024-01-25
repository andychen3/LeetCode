from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        odds = 0
        
        for counts in freq.values():
            if counts % 2:
                odds += 1
        
        if odds > 1:
            return len(s) - odds + 1
        return len(s)