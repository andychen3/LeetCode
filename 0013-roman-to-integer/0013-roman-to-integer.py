class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            char = s[i]
            if i + 1 < n and roman_map[char] < roman_map[s[i + 1]]:
                ans += roman_map[s[i + 1]] - roman_map[char]
                i += 2
            else:
                ans += roman_map[char]
                i += 1
        return ans
                
                