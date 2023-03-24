from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = defaultdict(int)
        ans = 0
        left = 0
        
        for right, val in enumerate(s):
            hash_table[val] += 1    
            while hash_table[val] > 1:
                left_char = s[left]
                hash_table[left_char] -= 1
                if hash_table[left_char] == 0:
                    del hash_table[left_char]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans