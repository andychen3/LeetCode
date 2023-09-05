class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # How would i know that this is a binary search problem?
        # One it can be a greedy problem because its looking for min integer. 
        # It cannot be dp because you can't build your answer based on previous
        # It's an array so we can potentially sort the array and because of that we can use binary search
        # Why would you not sort this?
        # Because a second way of using BS is based on solution space
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            
            # it is hours <= h because that means if you can complete it faster than h anything above this
            # eating speed will be possible. So we reduce right to find the threshold
            return hours <= h 
            

        left = 1 # Because koko has to eat at least one banana else you wouldn't deplete the pile
        right = max(piles) # Because if you can eat the max of the pile you can eat everything
        while left <= right:
            mid = (left + right) // 2
            # We check mid because we want to find that threshold where koko can eat the min amount of
            # bananas within h hours.
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # We return left because left will hold the insertion point of that threshold
        return left