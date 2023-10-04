from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = defaultdict(int)
        ans = left = 0

        for right in range(len(s)):
            hash_map[s[right]] += 1

            while hash_map[s[right]] > 1:
                hash_map[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans