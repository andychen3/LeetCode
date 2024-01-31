from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        seen = defaultdict(int)
        
        for right, char in enumerate(s):
            seen[char] += 1
            
            while seen[char] > 1:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
            
            