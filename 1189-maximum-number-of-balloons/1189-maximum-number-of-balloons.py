from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 7:
            return 0
        hash_map = defaultdict(int)
        
        for vals in text:
            if vals in "balon":
                hash_map[vals] += 1
        
        hash_map['l'] = hash_map['l'] // 2
        hash_map['o'] = hash_map['o'] // 2
        
        return min(hash_map.values()) if len(hash_map) == 5 else 0