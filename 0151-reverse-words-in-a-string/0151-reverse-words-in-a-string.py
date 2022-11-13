class Solution:
    def reverseWords(self, s: str) -> str:
        new = s.split()
        new.reverse()
        return " ".join(new)
        # print(new)
        # print(" ".join(new))
