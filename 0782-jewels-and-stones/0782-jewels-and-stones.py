class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        ans = 0

        for stone in stones:
            if stone in jewel:
                ans += 1
        return ans