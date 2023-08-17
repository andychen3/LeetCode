class Solution:
    def reverseWords(self, s: str) -> str:
        word_array = s.split(" ")
        ans = []
        
        for words in word_array:
            ans.append(self.reverse(list(words)))
        return " ".join(ans)


    
    def reverse(self, word):
        left, right = 0, len(word)-1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return "".join(word)
