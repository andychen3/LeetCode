class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0

        for index, char in enumerate(haystack):
            if char == needle[0]:
                left = index
                right = index
                needle_idx = 0
                while right < len(haystack) and needle_idx < len(needle):
                    if haystack[right] == needle[needle_idx]:
                        right += 1
                        needle_idx += 1
                    else:
                        break
                if needle_idx == len(needle):
                    return left
        return -1
                
                    
            