class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            
            while s[right] in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(s[right])
            
            longest = max(longest, right - left + 1)
            
        return longest