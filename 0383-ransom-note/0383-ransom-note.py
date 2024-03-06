class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        counts = Counter(magazine)
        
        for char in ransomNote:
            if char in counts and counts[char] > 0:
                counts[char] -= 1
            else:
                return False
        return True
                