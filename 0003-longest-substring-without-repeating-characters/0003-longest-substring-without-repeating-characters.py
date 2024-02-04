from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        hash_map = defaultdict(int)
        
        for right, char in enumerate(s):
            hash_map[char] +=1
            
            while hash_map[char] > 1:
                hash_map[s[left]] -= 1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        