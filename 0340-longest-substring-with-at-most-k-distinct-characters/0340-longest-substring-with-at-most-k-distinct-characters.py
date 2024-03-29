from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        ans = left = 0
        
        for right, char in enumerate(s):
            hash_map[char] += 1
            
            while len(hash_map) > k:
                hash_map[s[left]] -= 1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans