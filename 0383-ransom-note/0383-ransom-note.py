from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        magazine_count = Counter(magazine)
        
        for char in ransomNote:
            if char in magazine_count:
                magazine_count[char] -= 1
                if magazine_count[char] == 0:
                    del magazine_count[char]
            else:
                return False
        return True