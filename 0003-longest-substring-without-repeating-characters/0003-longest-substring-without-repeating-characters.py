class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        hash_set = set()
        
        for right, word in enumerate(s):
                
            while word in hash_set:
                left_word = s[left]
                hash_set.remove(left_word)
                left += 1
            
            hash_set.add(word)
            
            longest = max(longest, right - left + 1)
        
        return longest