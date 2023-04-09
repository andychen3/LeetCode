from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = defaultdict(int)
        longest = 0
        left = 0
        
        for right, word in enumerate(s):
            hash_map[word] += 1
            
            while hash_map[word] > 1:
                left_word = s[left]
                hash_map[left_word] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest