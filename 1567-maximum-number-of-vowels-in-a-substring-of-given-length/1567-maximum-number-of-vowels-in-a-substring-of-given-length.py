class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr = 0
        for i in range(k):
            if s[i] in 'aeiou':
                curr += 1
        
        ans = curr
        for right in range(k, len(s)):
            left_char = s[right - k]
            if s[right] in 'aeiou':
                curr += 1
            if left_char in 'aeiou':
                curr -= 1
            ans = max(curr, ans)
        return ans

        