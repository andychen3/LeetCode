from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        hash_map = defaultdict(int)
        
        for char in magazine:
            hash_map[char] += 1
        
        for char in ransomNote:
            if char in hash_map and hash_map[char] > 0:
                hash_map[char] -= 1
                if hash_map[char] == 0:
                    del hash_map[char]
            else:
                return False
        return True
        