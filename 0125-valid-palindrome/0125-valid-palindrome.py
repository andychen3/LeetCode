class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for char in s:
            if char.isalnum():
                new.append(char.lower())
        
        
        converted = "".join(new) 
        # print(reversed(converted))
        
        return converted == converted[::-1]
                