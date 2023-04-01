class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1
        
        def check(speed):
            time = 0
            
            for d in dist:
                time = ceil(time)
                time += d/speed
                
                
            return time <= hour
        
        left = 1
        right = 10**7
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            
            
        
        
        