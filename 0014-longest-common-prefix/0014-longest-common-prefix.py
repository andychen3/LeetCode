class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        for words in zip(*strs):
            if len(set(words)) == 1:
                ans += words[0]
            else:
                return ans
        return ans