from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_freq = 0
        char_map = defaultdict(int)
        ans = 0
        
        for right, char in enumerate(s):
            char_map[char] += 1
            max_freq = max(max_freq, char_map[char])
            
            while (right - left + 1) - max_freq > k:
                char_map[s[left]] -= 1
                
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans