class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(rate):
            hours = 0
            
            for pile in piles:
                hours += ceil(pile / rate)
            
            return hours <= h
        
        left = 1
        right = max(piles)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if (check(mid)):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res