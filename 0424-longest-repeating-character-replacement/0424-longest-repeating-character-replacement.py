from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        hash_map = defaultdict(int)
        left = 0
        max_length = 0
        
        for right, word in enumerate(s):
            hash_map[word] += 1
            max_freq = max(max_freq, hash_map[word])
            
            while right - left + 1 - max_freq > k:
                left_word = s[left]
                hash_map[left_word] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        return max_length