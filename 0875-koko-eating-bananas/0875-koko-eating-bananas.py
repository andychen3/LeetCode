class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hour = 0
            
            for pile in piles:
                hour += ceil(pile / k)
            
            return hour <= h
        
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left