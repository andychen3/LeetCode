class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0

        for num in gain:
            curr += num
            highest = max(highest, curr)
        return highest