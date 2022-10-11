class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_hash = collections.Counter(s)
        res = -1
        
        for index, char in enumerate(s):
            if s_hash[char] == 1:
                res = index
                return index
        return res
        