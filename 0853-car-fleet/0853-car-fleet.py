class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        stack = []
        
        for p, s in sorted(pairs):
            time_to_arrive = (target - p) / s
            
            while stack and stack[-1] <= time_to_arrive:
                stack.pop()
            stack.append(time_to_arrive)
        
        return len(stack)