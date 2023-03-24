class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_hash = collections.Counter(magazine)
        
        for letters in ransomNote:
            if letters not in magazine_hash:
                return False
            magazine_hash[letters] -= 1
            if magazine_hash[letters] == 0:
                del magazine_hash[letters]
        
        return True