class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_set = set()
        
        for char in s:
            if char in hash_set:
                hash_set.remove(char)
            else:
                hash_set.add(char)
        
        return len(s)-len(hash_set)+1 if len(hash_set) > 1 else len(s)
        