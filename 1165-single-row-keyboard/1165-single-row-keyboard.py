class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hash_map = defaultdict(int)
        
        for index, val in enumerate(keyboard):
            hash_map[val] = index
            
        total = 0
        start = 0
        
        for char in word:
            total += abs(hash_map[char]-start)
            start = hash_map[char]
        
        return total
            
            