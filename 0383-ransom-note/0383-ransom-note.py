class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
              
        ransom_dict.subtract(magazine_dict)
        print(ransom_dict)
        
        for x in ransom_dict.values():
            if x > 0:
                return False
            
        return True
