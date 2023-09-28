class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        left = right = 0
        string = []

        while left < len_word1 and right < len_word2: 
            string.append(word1[left])
            string.append(word2[right])
            left += 1
            right += 1
        
        while left < len_word1:
            string.append(word1[left])
            left += 1

        while right < len_word2:
            string.append(word2[right])
            right += 1
        
        return "".join(string)