from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern = Counter(t)
        countS = defaultdict(int)
        
        missing = len(pattern)
        have = 0
        
        res = [-1,-1]
        resLen = float("inf")
        left = 0
        
        for right, char in enumerate(s):
            countS[char] += 1
            
            if char in pattern and countS[char] == pattern[char]:
                have += 1
            
            while have == missing:
                if right - left + 1 < resLen:
                    res = [left, right + 1]
                    resLen = right - left + 1
                left_char = s[left]
                countS[left_char] -= 1
                if left_char in pattern and countS[left_char] < pattern[left_char]:
                    have -= 1
                left += 1
                
        x, y = res
        return s[x:y] if resLen != float('inf') else ""