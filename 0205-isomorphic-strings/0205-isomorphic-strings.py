class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = collections.defaultdict()
        hash_t = collections.defaultdict()
        
        for index, char in enumerate(s):
            if char not in hash_s and t[index] not in hash_t:
                hash_s[char] = t[index]
                hash_t[t[index]] = char
            if hash_s.get(char) != t[index] or hash_t.get(t[index]) != char:
                return False
        return True
        

                
                
            
            
        