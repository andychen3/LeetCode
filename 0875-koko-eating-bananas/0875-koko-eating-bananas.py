class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) > h:
        #     return -1
        
        def check(speed):
            time = 0
            
            for pile in piles:
                
                time += ceil(pile/speed)
                
            return time <= h
        
        left = 1
        right = max(piles)
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        