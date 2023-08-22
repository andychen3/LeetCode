class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            # Check if there are asteroids in stack and if top asteroid is positive
            # while the current asteroid is negative
            while stack and stack[-1] > 0 and asteroid < 0:
                # Check if the top asteroid is smaller than the left moving asteroid
                if stack[-1] + asteroid < 0:
                    stack.pop()
                # If the top asteroid is bigger than the left moving skip
                elif stack[-1] + asteroid > 0:
                    break
                # both are the same size so pop top asteroid
                else:
                    stack.pop()
                    break
            # Else add the asteroid since they are all facing the same direction
            else:
                stack.append(asteroid)
        return stack

