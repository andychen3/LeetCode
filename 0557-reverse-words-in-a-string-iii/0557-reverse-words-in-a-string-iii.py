class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        return " ".join([char[::-1] for char in word])