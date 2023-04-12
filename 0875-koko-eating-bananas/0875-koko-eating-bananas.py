class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(rate):
            hours = 0
            
            for banana in piles:
                hours += ceil(banana/rate)
                
            return hours <= h
        
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left