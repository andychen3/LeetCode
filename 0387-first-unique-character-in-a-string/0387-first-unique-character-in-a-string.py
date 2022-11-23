class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        
        for index, char in enumerate(s):
            if s_count[char] == 1:
                return index
            
        return -1
            

        