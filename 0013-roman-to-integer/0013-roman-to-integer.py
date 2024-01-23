class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            char = s[i]
            if i + 1 < n and char == "I" and (s[i + 1] == 'V' or s[i + 1] == "X"):
                ans += roman_map[s[i + 1]] - roman_map[char]
                i += 2
            elif i + 1 < n and char == "X" and (s[i + 1] == 'L' or s[i + 1] == "C"):
                ans += roman_map[s[i + 1]] - roman_map[char]
                i += 2
            elif i + 1 < n and char == "C" and (s[i + 1] == 'D' or s[i + 1] == "M"):
                ans += roman_map[s[i + 1]] - roman_map[char]
                i += 2
            else:
                ans += roman_map[char]
                i += 1
        return ans
                
                