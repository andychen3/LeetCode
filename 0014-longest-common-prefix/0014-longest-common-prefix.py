class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for char in zip(*strs):
            if len(set(char)) != 1:
                break
            else:
                prefix += char[0]
        return prefix
