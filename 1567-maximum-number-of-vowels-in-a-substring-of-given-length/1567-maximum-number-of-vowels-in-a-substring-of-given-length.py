class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # To simplify this because doing in 'aeiou' is k times. We can simplify this
        # by having a hashset to reduce the in operator to 0(1)
        # To simplify the logic some more we can convert s[right] into just adding it to curr
        # The reasoning is everytime you check if a char in s is a vowel in the set it will return 0 or 1.
        # This is because it will say true or false which can be converted to its numerical value
        vowels = set("aeiou")

        curr = 0
        for i in range(k):
            curr += s[i] in vowels
        
        ans = curr
        for right in range(k, len(s)):
            curr += s[right] in vowels
            # It is right - k because we are starting at k. and we already preprocessed the starting length
            # up to k. So in the example k == 3 then the starting right value is also 3. right - k is
            # 3-3 = 0 which gives you the first index. as you increment forward right will increase
            # which will give you the leftmost index everytime
            curr -= s[right - k] in vowels
            ans = max(curr, ans)
        return ans

        