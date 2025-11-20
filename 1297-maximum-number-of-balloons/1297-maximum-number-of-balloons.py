class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {}

        for char in text:
            if char in 'balloon':
                if char not in counts:
                    counts[char] = 0
            
                counts[char] += 1        
        
        if len(counts) < 5:
            return 0
        
        counts['l'] //= 2
        counts['o'] //= 2

        return min(counts.values())