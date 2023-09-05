class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        # This can be greedy because its asking for maximum. 
        weight.sort()
        capacity = 5000
        count = 0

        for mass in weight:
            if capacity - mass >= 0:
                count += 1
                capacity -= mass
        return count