class Solution:
    def toLowerCase(self, s: str) -> str:
        string = []

        for char in s:
            string.append(char.lower())
        return "".join(string)