class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goal = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, val in enumerate(t):
                if val == target[i]:
                    goal.add(i)
        return len(goal) == 3