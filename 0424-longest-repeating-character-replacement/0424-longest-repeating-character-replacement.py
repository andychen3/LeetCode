from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        ans = max_freq = left = 0
        
        for right, char in enumerate(s):
            hash_map[char] += 1
            max_freq = max(max_freq, hash_map[char])
            
            while (right - left + 1) - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1
        
        return right - left + 1