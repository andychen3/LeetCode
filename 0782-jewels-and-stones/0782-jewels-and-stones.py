class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        rocks = set(jewels)
        ans = 0
        for stone in stones:
            if stone in rocks:
                ans += 1
        return ans
