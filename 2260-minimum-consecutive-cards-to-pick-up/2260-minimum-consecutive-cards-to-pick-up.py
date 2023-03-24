
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = len(cards)+1
        hash_map = defaultdict(int)
        left = 0
        
        for right, card in enumerate(cards):
            hash_map[card] += 1
            while hash_map[card] == 2:
                ans = min(right - left + 1, ans)
                hash_map[cards[left]] -= 1
                if hash_map[cards[left]] == 0:
                    del hash_map[cards[left]]
                left += 1
        return ans if ans <= len(cards) else -1
        
        
        
        