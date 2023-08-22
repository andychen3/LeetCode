class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for asteroid in asteroids:
            # Check if asteroid is moving to the right or stack is empty
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                # Handle collisions with asteroids moving to the left
                while stack and stack[-1] > 0:
                    top_asteroid = stack.pop()
                    if abs(top_asteroid) == abs(asteroid):
                        # Both asteroids explode
                        break
                    elif abs(top_asteroid) > abs(asteroid):
                        # Top asteroid survives and current asteroid explodes
                        stack.append(top_asteroid)
                        break
                else:
                    # The current asteroid survives and is moving to the left
                    stack.append(asteroid)
        
        return stack