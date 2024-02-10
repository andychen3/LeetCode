class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        i = 0
        ans = 0
        n = len(s)
        
        while i < n:
            if i + 1 < n and numerals[s[i]] < numerals[s[i+1]]:
                ans += numerals[s[i+1]] - numerals[s[i]]
                i += 2
            else:
                ans += numerals[s[i]]
                i += 1
        return ans