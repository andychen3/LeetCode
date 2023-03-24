
from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash_cards = defaultdict(list)
        
        for index, card in enumerate(cards):
            hash_cards[card].append(index)
            
        ans = len(cards)+1
        for pairs in hash_cards.values():
            n = len(pairs)
            for i in range(n-1):
                ans = min(ans, pairs[i+1] - pairs[i] + 1)
        return ans if ans <= len(cards) else -1
        
        
        
#         ans = len(cards)+1
#         hash_map = defaultdict(int)
#         left = 0
        
#         for right, card in enumerate(cards):
#             hash_map[card] += 1
#             while hash_map[card] == 2:
#                 ans = min(right - left + 1, ans)
#                 hash_map[cards[left]] -= 1
#                 if hash_map[cards[left]] == 0:
#                     del hash_map[cards[left]]
#                 left += 1
#         return ans if ans <= len(cards) else -1
        
        
        
        