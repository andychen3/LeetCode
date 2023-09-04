import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # What do i know about this problem?
        # Could be a heap problem since it says at most k distinct projects
        # Also could be greedy and use of heap since you are trying to maximize your final capital 
        # So everytime you get a project the next project if same cost you want the highest profit.
        choices = sorted(zip(capital, profits))
        heap = []
        i = 0 # Iterate through the sorted choices
        n = len(choices)

        for _ in range(k): # Iterate up to k times
            while i < n and choices[i][0] <= w: # Check which projects you can afford
                heapq.heappush(heap, -choices[i][1]) # Add the projects onto the max heap
                i += 1
            # If no more available projects return profits
            if len(heap) == 0:
                return w

            # Pop from max heap and add to profits
            w -= heapq.heappop(heap)
        
        return w