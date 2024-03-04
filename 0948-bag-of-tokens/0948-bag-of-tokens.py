class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        ans = 0
        
        left, right = 0, len(tokens) - 1
        while left <= right:

            if power >= tokens[left]:
                ans += 1
                power -= tokens[left]
                left += 1
            elif left < right and ans > 0:
                ans -= 1
                power += tokens[right]
                right -= 1
            else:
                return ans
        return ans