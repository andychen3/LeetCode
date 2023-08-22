class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while stack and stack[-1] > 0 and rock < 0:
                if stack[-1] + rock == 0:
                    stack.pop()
                    break
                elif stack[-1] + rock > 0:
                    break
                elif stack[-1] + rock < 0:
                    stack.pop()
                    
            else:
                stack.append(rock)
        return stack