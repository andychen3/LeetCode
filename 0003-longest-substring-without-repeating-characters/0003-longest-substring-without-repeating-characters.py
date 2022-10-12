class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest_sub = 0
        window_start = 0
        
        for window_end, char in enumerate(s):    
            while char in char_set:
                char_set.remove(s[window_start])
                window_start += 1
            
            char_set.add(char)
            longest_sub = max(longest_sub, len(char_set))
            
            
        return longest_sub
            
