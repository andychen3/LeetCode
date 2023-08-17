class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr_gain = 0

        for i in range(len(gain)):
            curr_gain += gain[i]
            max_alt = max(curr_gain, max_alt)
        
        return max_alt
