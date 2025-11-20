class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        counts = set()

        for right, char in enumerate(s):
            while char in counts:
                counts.remove(s[left])
                left += 1

            counts.add(char)

            ans = max(ans, right - left + 1)

        return ans        