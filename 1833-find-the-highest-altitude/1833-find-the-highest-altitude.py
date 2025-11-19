class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        highest = 0

        for height in gain:
            total += height
            highest = max(total, highest)
        
        return highest