from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        mag_counts = Counter(magazine)
        
        for char in ransomNote:
            if char in mag_counts:
                mag_counts[char] -= 1
                if mag_counts[char] == 0:
                    del mag_counts[char]
            else:
                return False
        return True