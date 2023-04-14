class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0
        cost = 0
        left = 0
        
        for right, char in enumerate(s):
            cost += abs(ord(char) - ord(t[right]))
            
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length