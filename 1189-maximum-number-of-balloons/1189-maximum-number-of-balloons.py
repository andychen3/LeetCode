class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_hash = collections.defaultdict(int)
        
        for char in text:
            if char in 'balloon':
                balloon_hash[char] += 1
        balloon_hash['l'] //= 2
        balloon_hash['o'] //= 2
        return min(balloon_hash.values()) if len(balloon_hash) == 5 else 0
        
        
                
        
        