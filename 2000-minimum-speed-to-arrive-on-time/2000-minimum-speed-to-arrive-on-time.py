class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # The reason this is binary search even though it says min positive integer
        # is because you are looking for a threshold speed that the trains can go at to 
        # make it within hours.
        # It is greedy for the check function
        # another giveaway is when it says answer will not exceed 10^7 which is giving you a max 
        # right bound.
        
        # Why is it ceil of hour?
        # It's ceil of hour because of the edge case where there are 3 trains and an hour of 2.7
        # The third train can technically be less than an hour since you can cover it in less than the time
        if len(dist) > ceil(hour):
            return -1
        
        def check(speed):
            time = 0
            for distance in dist:
                
                time = math.ceil(time)
                # We don't round up during every trip. Only when we wait for the next train
                # because every train departs on the closest hour
                time += (distance / speed)
            # The reason it's time is less or equal to hour because that means you made it given
            # the speed    
            return time <= hour


        left = 1
        right = 10 **7
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left