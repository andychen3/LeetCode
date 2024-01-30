class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        for word in zip(*strs):
            if len(set(word)) == 1:
                ans += word[0]
            else:
                return ans
        return ans