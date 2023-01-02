class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # check if all lower
        if word.islower():
            return True
        elif word.isupper():
            return True
        elif word[0].isupper():
            if word[1:].islower() or word[1:].isupper():
                return True
            else:
                return False
    
        return False
        
        # check if all upper
        
        # check if the first is upper case and the rest is all upper