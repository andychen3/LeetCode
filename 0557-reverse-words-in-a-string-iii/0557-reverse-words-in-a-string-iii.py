class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        return " ".join([words[::-1] for words in word])