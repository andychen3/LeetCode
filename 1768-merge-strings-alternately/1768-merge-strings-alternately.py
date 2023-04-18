class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left_1 = 0
        left_2 = 0
        ans = []
        
        while left_1 < len(word1) and left_2 < len(word2):
            ans.append(word1[left_1])
            ans.append(word2[left_2])
            left_1 += 1
            left_2 += 1
        
        if left_1 < len(word1):
            for char in word1[left_1:]:
                ans.append(char)
        
        if left_2 < len(word2):
            for char in word2[left_2:]:
                ans.append(char)
        
        return "".join(ans)
            