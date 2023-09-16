class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # To simplify this because doing in 'aeiou' is k times. We can simplify this
        # by having a hashset to reduce the in operator to 0(1)
        vowels = set("aeiou")

        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        
        ans = curr
        for right in range(k, len(s)):
            left_char = s[right - k]
            if s[right] in vowels:
                curr += 1
            if left_char in vowels:
                curr -= 1
            ans = max(curr, ans)
        return ans

        