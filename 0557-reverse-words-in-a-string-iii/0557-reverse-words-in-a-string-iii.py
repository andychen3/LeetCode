class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join([word[::-1] for word in arr])