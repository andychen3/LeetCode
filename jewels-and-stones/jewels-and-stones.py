from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        ans = 0
        
        for rocks in counter:
            if rocks in jewels:
                ans += counter[rocks]
                
        return ans
        