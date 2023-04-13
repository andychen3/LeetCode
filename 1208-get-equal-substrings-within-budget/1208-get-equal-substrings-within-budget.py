class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = 0
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            cost += abs(ord(t[right]) - ord(char))
            
            while cost > maxCost:
                cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1               
            
            max_length = max(max_length, right - left + 1)
            
            
        
        return max_length
        