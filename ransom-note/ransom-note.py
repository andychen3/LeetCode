class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)
              
        ransom_dict.subtract(magazine_dict)
        
        for x in ransom_dict.values():
            if x > 0:
                return False
            
        return True

    
#         char_frequency = {}
        
#         for char in magazine:
#             char_frequency[char] = char_frequency.get(char, 0) + 1
            
#         for elements in ransomNote:
#             if elements in char_frequency and char_frequency[elements] != 0:
#                 char_frequency[elements] -= 1
#             else:
#                 return False
            
#         return True