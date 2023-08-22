class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            # Check if there are asteroids on stack and if the top is positive and next rock is negative
            while stack and stack[-1] > 0 and rock < 0:
                # if both are same size break both and move on
                if stack[-1] + rock == 0:
                    stack.pop()
                    break
                # if top rock is greater than coming rock move on
                elif stack[-1] + rock > 0:
                    break
                # if rock is bigger than top rock break top rock and keep checking stack
                elif stack[-1] + rock < 0:
                    stack.pop()
            # If stack is empty or positive rock add to stack.
            else:
                stack.append(rock)
        return stack