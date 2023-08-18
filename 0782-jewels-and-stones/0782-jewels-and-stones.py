from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counts = Counter(stones)
        total = sum(stone_counts[jewel] for jewel in jewels)

        return total
        