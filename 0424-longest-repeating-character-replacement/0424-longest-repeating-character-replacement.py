from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)
        max_char = 0
        left = 0
        longest = 0
        
        for right, word in enumerate(s):
            hash_map[word] += 1
            
            max_char = max(max_char, hash_map[word])
            
            while right - left + 1 - max_char > k:
                left_word = s[left]
                hash_map[left_word] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest